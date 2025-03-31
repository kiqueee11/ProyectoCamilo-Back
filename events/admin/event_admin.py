from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','location', 'created_at', 'updated_at', 'host')
    filter_horizontal = ('users',)
    search_fields = ('name', 'location')
    list_filter = ('location', 'title')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

admin.site.register(Event, EventAdmin)