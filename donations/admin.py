from django.contrib import admin
from donations.models import Donations, Donors, Expenses, Products, Items
from donations.form import ItemsForm


class DonorsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)
    list_filter = ['name', 'created_at']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ('name', 'description',)
    list_filter = ['name', 'created_at']


class DonationsAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'donor', 'date', 'quantity',
                    'created_at']
    search_fields = ('name__name', 'service_type',)
    list_filter = ['service_type', 'created_at']


class ItemsInline(admin.TabularInline):
    model = Items
    form = ItemsForm
    extra = 1


class ExpensesAdmin(admin.ModelAdmin):
    inlines = [ItemsInline]
    list_display = ['name', 'service_type', 'date']
    search_fields = ('name__name', 'service_type',)
    list_filter = ['service_type', 'created_at']


admin.site.register(Donations, DonationsAdmin)
admin.site.register(Donors, DonorsAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Products, ProductsAdmin)
