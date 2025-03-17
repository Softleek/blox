import django_filters as filters
from frappe_app.models.automation.milestone import Milestone

class MilestoneFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Milestone
        fields = ['id']

