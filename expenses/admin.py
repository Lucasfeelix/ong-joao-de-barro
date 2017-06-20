from django.contrib import admin
from expenses.models import Expenses


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['service_type', 'item', 'description', 'quantity', 'price',
                    'total', 'created_at']
    search_fields = ('service_type',)
    list_filter = ['service_type', 'created_at']


admin.site.register(Expenses, ExpensesAdmin)
