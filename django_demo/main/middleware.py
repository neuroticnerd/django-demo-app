"""
Add user created_by and modified_by foreign key refs
to any model automatically.

Almost entirely taken from:
https://github.com/Atomidata/django-audit-log/blob/master/audit_log/
middleware.py
"""
from django.db.models import signals
from django.utils import timezone
from django.utils.functional import curry


class ModifiedByMiddleware(object):
    def process_request(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated():
            user = request.user
        else:
            user = None

        modifier = curry(self.modifier, user)
        signals.pre_save.connect(
            modifier,
            dispatch_uid=(self.__class__, request,),
            weak=False
        )

    def process_response(self, request, response):
        signals.pre_save.disconnect(
            dispatch_uid=(self.__class__, request,)
        )
        return response

    def modifier(self, user, sender, instance, **kwargs):
        if not getattr(instance, 'created_by_id', None):
            instance.created_by = user
        if hasattr(instance, 'modified_by_id'):
            instance.modified_by = user
        instance.modified_at = timezone.now()
