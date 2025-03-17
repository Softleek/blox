import django_filters as filters
from frappe_app.models.core.log_setting_user import LogSettingUser

class LogSettingUserFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = LogSettingUser
        fields = ['id']

