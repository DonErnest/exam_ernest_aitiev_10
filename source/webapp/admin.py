from django.contrib import admin

from webapp.models import SharedFile


class FileModelAdmin(admin.ModelAdmin):
    fields = ['name', 'file', 'sharing_type', 'user_id', 'uploaded', 'downloaded_count', 'privately_accessed']
    list_display = ['id', 'name', 'file', 'sharing_type', 'user_id', 'uploaded', 'downloaded_count']
    list_filter = ['user_id', 'sharing_type']
    readonly_fields = ['uploaded']
    search_fields = ['name']


admin.site.register(SharedFile, FileModelAdmin)
