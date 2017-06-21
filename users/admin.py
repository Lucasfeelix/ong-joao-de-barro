# coding=utf-8
from django.contrib import admin
from users.models import Donors


class DonorsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'address', 'number',
                       'complement', 'neighborhood', 'city', 'state', 'cep', )
        }),
    )
    list_display = ['name']
    search_fields = ('name',)
    list_filter = ['name', 'created_at']


admin.site.register(Donors, DonorsAdmin)
