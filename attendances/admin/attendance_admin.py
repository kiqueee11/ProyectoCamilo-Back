from django.contrib import admin

from attendances.models.attendance_model import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'user', 'attendance',)
    search_fields = ('event', 'user',)

    list_filter = ('event',)
    ordering = ('-updated_at',)

admin.site.register(Attendance, AttendanceAdmin)