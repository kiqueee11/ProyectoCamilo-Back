from django.contrib import admin

from attendances.models.attendance_model import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'user', 'attendance',)

    list_filter = ('event',)
    ordering = ('-updated_at',)

admin.site.register(Attendance, AttendanceAdmin)