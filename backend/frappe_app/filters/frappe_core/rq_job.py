import django_filters as filters
from frappe_app.models.frappe_core.rq_job import RQJob

class RQJobFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = RQJob
        fields = ['id']

