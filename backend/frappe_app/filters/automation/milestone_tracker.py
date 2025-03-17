import django_filters as filters
from frappe_app.models.automation.milestone_tracker import MilestoneTracker

class MilestoneTrackerFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = MilestoneTracker
        fields = ['id']

