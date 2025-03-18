import django_filters as filters
from frappe_app.models.frappe_core.transaction_log import TransactionLog

class TransactionLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = TransactionLog
        fields = ['id']

