from django.db import models
import secrets


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
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