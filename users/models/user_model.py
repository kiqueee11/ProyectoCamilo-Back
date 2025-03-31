import secrets

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.text import slugify
from events.models import Event


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Usuario debe de tener un correo electrónico")
        if not password:
            raise ValueError("Ingrese una contraseña por favor")

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email = email, password = password, **extra_fields)

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Correo electrónico", null=False)
    phone = models.CharField(max_length=20, unique=True, verbose_name="Número de telefono")
    password = models.CharField(max_length=150, verbose_name="Contraseña", null=False)
    slug = models.SlugField(max_length=50, unique=True, verbose_name="slug", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="¿El usuario esta activo?")
    is_staff = models.BooleanField(default=False, verbose_name="Autorizado para ser staff")
    is_superuser = models.BooleanField(default=False, verbose_name="¿Es administrador?")

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table="Users"
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            cont = 1

            while CustomUser.objects.filter(slug=slug).exists():
                slug = f"{slug}-{cont}"
                cont+=1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.email}"