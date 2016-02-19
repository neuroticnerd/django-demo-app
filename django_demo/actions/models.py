from django.contrib.auth.models import User
from django.db import models

from django_demo.main.modelutils import ModifiedByMixin, TimestampMixin


class Action(ModifiedByMixin, TimestampMixin):
    title = models.CharField(max_length=256, verbose_name='Action')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title


class ActionAssignment(ModifiedByMixin, TimestampMixin):
    action = models.ForeignKey(
        Action,
        related_name='assigned_to',
        verbose_name='Action'
    )
    user = models.ForeignKey(
        User,
        related_name='assignments',
        verbose_name='User'
    )

    def __str__(self):
        return str(self.action) + ' --> ' + str(self.user)

    class Meta:
        unique_together = (('action', 'user'),)
