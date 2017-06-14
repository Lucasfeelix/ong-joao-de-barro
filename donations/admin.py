from django.contrib import admin
from donations.models import Donations, Donors
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


admin.site.register(Donations, DonationsAdmin)
admin.site.register(Donors, DonorsAdmin)
