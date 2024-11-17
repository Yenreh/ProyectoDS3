from django.contrib import admin
from .models import Transaction
from .models import Appointment, AppointmentHistory

admin.site.register(Appointment)
admin.site.register(AppointmentHistory)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('transaction_id',)
