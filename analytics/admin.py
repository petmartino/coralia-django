from django.contrib import admin
from .models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'path', 'status_code', 'ip_address', 'session_key')
    list_filter = ('status_code', 'timestamp')
    search_fields = ('path', 'ip_address')
    list_per_page = 50