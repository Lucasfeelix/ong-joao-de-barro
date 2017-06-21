from django.contrib import admin
from donations.models import Donations, Donors
# from donations.forms import ExpensesForm


class DonationsAdmin(admin.ModelAdmin):
    list_display = ['service_type', 'donor', 'item', 'description', 'quantity',
                    'created_at']
    search_fields = ('service_type', 'donor', 'item')
    list_filter = ['service_type', 'created_at']


admin.site.register(Donations, DonationsAdmin)
