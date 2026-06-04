from django.contrib import admin
from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'target_audience', 'priority', 'is_active', 'expires_at', 'created_by', 'created_at')
    list_filter = ('target_audience', 'priority', 'is_active')
    search_fields = ('title', 'message')
    actions = ['deactivate_announcements']

    def deactivate_announcements(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_announcements.short_description = 'Deactivate selected announcements'
