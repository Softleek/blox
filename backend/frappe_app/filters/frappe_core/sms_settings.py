import django_filters as filters
from frappe_app.models.frappe_core.sms_settings import SMSSettings

class SMSSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SMSSettings
        fields = ['id']

