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


class ActionAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        'action', 'user', 'created_by', 'created_at',
    )
    fields = ('action', 'user', 'created_at', 'modified_at')
    readonly_fields = (
        'created_by', 'modified_by',
    )


admin.site.register(models.Action, ActionAdmin)
admin.site.register(models.ActionAssignment, ActionAssignmentAdmin)
