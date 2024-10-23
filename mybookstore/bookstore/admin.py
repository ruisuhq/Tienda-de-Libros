from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, CartItem

class UserProfileAdmin(UserAdmin):
    # Campos que se mostrarán en la lista de usuarios en el panel de administración
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Campos que se pueden buscar en el panel de administración
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Campos que serán editables directamente desde la lista de usuarios
    list_editable = ('is_staff',)

    # Secciones y campos que se mostrarán al editar un usuario en el panel de administración
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'profile_image', 'description')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos que se mostrarán al crear un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'profile_image', 'description'),
        }),
    )

admin.site.register(CartItem)
admin.site.register(UserProfile, UserAdmin)