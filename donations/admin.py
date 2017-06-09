from django.contrib import admin
from donations.models import Donations, Donors, Expenses
# from donations.forms import ExpensesForm


class DonorsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)
    list_filter = ['name', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


class DonationsAdmin(admin.ModelAdmin):
    list_display = ['service_type', 'donor', 'item', 'description', 'date',
                    'quantity', 'created_at']
    search_fields = ('service_type', 'donor', 'item')
    list_filter = ['service_type', 'created_at']
    

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['service_type', 'item', 'description', 'quantity', 'price',
                    'total', 'date', 'created_at']
    search_fields = ('service_type',)
    list_filter = ['service_type', 'created_at']
    # forms = ExpensesForm


admin.site.register(Donations, DonationsAdmin)
admin.site.register(Donors, DonorsAdmin)
admin.site.register(Expenses, ExpensesAdmin)
