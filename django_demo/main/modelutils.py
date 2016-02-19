from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def get_creation_time():
    """
    I initially created this as a quick lambda inline of the field declaration
    but apparently migrations do not play well at all with lambdas, so to avoid
    migration issues this is now a separate function
    """
    return timezone.now()


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        default=get_creation_time,
        verbose_name='Creation Time'
    )
    modified_at = models.DateTimeField(
        default=get_creation_time,
        verbose_name='Last Modified'
    )

    class Meta:
        abstract = True
        get_latest_by = 'created_at'


class ModifiedByMixin(models.Model):
    created_by = models.ForeignKey(
        User,
        verbose_name='Author',
        related_name='created_%(class)ss',
    )
    modified_by = models.ForeignKey(
        User,
        verbose_name='Modified By',
        related_name='modified_%(class)ss',
    )

    class Meta:
        abstract = True
