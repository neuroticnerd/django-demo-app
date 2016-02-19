from django.contrib import admin

from . import models


class ActionAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'created_by', 'created_at', 'modified_by', 'modified_at'
    )
    list_filter = ('created_by', 'created_at')
    fields = ('title', 'description')
    readonly_fields = (
        'created_by', 'created_at', 'modified_by', 'modified_at'
    )


admin.site.register(models.Action, ActionAdmin)
