from django.contrib import admin

from users.models import CustomUser

class UserAdmin(admin.ModelAdmin):
    model = CustomUser

    list_display = ('id', 'name', 'email', 'phone', 'is_active', 'is_superuser')
    list_filter = ('is_active', 'is_superuser', 'is_staff')
    search_fields = ('name', 'email',)

    ordering = ('name',)

    list_editable = ('is_active', 'is_superuser')

    fieldsets = (
        ('Información del usuario', {'fields': ('name', 'email', 'phone', 'password')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        ("Creación de usuario", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')
        })
    )

admin.site.register(CustomUser, UserAdmin)
