from django.contrib import admin
from donations.models import Donations, Donors, Expenses, ItemsExpenses, ItemsDonations
from donations.form import ItemsForm


class DonorsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)
    list_filter = ['name', 'created_at']


class ItemsDonationsInline(admin.TabularInline):
    model = ItemsDonations
    extra = 1


class DonationsAdmin(admin.ModelAdmin):
    inlines = [ItemsDonationsInline]
    list_display = ['service_type', 'donor', 'date', 'quantity',
                    'created_at']
    search_fields = ('service_type',)
    list_filter = ['service_type', 'created_at']


class ItemsExpensesInline(admin.TabularInline):
    model = ItemsExpenses
    form = ItemsForm
    extra = 1


class ExpensesAdmin(admin.ModelAdmin):
    inlines = [ItemsExpensesInline]
    list_display = ['service_type', 'date']
    search_fields = ('service_type',)
    list_filter = ['service_type', 'created_at']


admin.site.register(Donations, DonationsAdmin)
admin.site.register(Donors, DonorsAdmin)
admin.site.register(Expenses, ExpensesAdmin)
