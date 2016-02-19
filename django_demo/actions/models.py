from django.db import models

from django_demo.main.modelutils import ModifiedByMixin, TimestampMixin


class Action(ModifiedByMixin, TimestampMixin):
    title = models.CharField(max_length=256, verbose_name='Action')
    description = models.TextField(verbose_name='Description')
