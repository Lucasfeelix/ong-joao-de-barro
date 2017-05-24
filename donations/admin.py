from django.contrib import admin
from donations.models import Donations, Donors, Expenses, Products


class DonorsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)
    list_filter = ['name', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ('name', 'description',)
    list_filter = ['name', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


class DonationsAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'donor', 'date', 'quantity',
                    'created_at']
    search_fields = ('name', 'service_type',)
    list_filter = ['service_type', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'date', 'quantity', 'price',
                    'total']
    search_fields = ('name', 'service_type',)
    list_filter = ['service_type', 'created_at']
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(Donations, DonationsAdmin)
admin.site.register(Donors, DonorsAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Products, ProductsAdmin)
