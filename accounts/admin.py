# coding=utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
from accounts.forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):
    """
    Classe para que seja possível acessar app de Usuários do Django
    Params:
        form = formulário de edição do objeto
    """
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'last_login')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                )
            }
        ),
    )
    list_display = ['username', 'name', 'email', 'is_active', 'is_staff',
                    'date_joined']


admin.site.register(User, UserAdmin)
