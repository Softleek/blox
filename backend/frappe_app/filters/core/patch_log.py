import django_filters as filters
from frappe_app.models.core.patch_log import PatchLog

class PatchLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PatchLog
        fields = ['id']

