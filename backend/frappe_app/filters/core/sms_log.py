import django_filters as filters
from frappe_app.models.core.sms_log import SMSLog

class SMSLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SMSLog
        fields = ['id']

