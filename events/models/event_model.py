from django.conf import settings
from django.db import models
import secrets

from backend.settings import AUTH_USER_MODEL


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,related_name='organizer', verbose_name="Organizador del evento", null=True, blank=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events', blank=True)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stars = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "events"
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_urlsafe(16)
            while Event.objects.filter(slug=prov).exists():
                prov = secrets.token_urlsafe(16)
            self.slug = prov
        super().save(*args, **kwargs)  # Corrected syntax

    def __str__(self):
        return self.title