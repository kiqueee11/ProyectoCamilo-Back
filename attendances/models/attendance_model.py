import secrets

from django.db import models

from users.models import CustomUser


class Attendance(models.Model):
    event = models.ForeignKey('Event', on_delete=models.RESTRICT, null=True, blank=True, related_name='attendances', verbose_name='Evento')
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, blank=True, related_name='attendances', verbose_name='Usuario')
    attendance = models.BooleanField(default=False, null=False, blank=False, verbose_name="Asistencia")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'attendances'
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        return f"{self.event} - {self.user} - {self.attendance}"



