import django_filters as filters
from frappe_app.models.desk.bulk_update import BulkUpdate

class BulkUpdateFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = BulkUpdate
        fields = ['id']

