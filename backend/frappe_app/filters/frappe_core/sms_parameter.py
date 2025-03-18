import django_filters as filters
from frappe_app.models.frappe_core.sms_parameter import SMSParameter

class SMSParameterFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SMSParameter
        fields = ['id']

