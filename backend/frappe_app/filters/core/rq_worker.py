import django_filters as filters
from frappe_app.models.core.rq_worker import RQWorker

class RQWorkerFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = RQWorker
        fields = ['id']

