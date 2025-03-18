import django_filters as filters
from frappe_app.models.frappe_core.view_log import ViewLog

class ViewLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ViewLog
        fields = ['id']

