import django_filters as filters
from frappe_app.models.core.submission_queue import SubmissionQueue

class SubmissionQueueFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SubmissionQueue
        fields = ['id']

