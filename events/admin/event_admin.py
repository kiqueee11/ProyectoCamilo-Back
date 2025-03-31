from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('slug','id', 'title','location', 'created_at', 'updated_at')
    search_fields = ('name', 'location')
    list_filter = ('location', 'title')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    readonly_fields = ('created_at', 'updated_at','slug')

admin.site.register(Event, EventAdmin)