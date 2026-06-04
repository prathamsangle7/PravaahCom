from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'related_module', 'related_id', 'file_type', 'file_size_kb', 'download_count', 'uploaded_by', 'uploaded_at')
    list_filter = ('related_module', 'file_type', 'uploaded_by')
    search_fields = ('title', 'related_module', 'related_id')
    readonly_fields = ('download_count', 'uploaded_at')
