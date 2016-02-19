from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic


class AuthenticatedView(generic.View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedView, self).dispatch(
            request, *args, **kwargs
        )
