from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.automation.milestone_tracker import MilestoneTracker
from frappe_app.filters.automation.milestone_tracker import MilestoneTrackerFilter
from frappe_app.serializers.automation.milestone_tracker import MilestoneTrackerSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class MilestoneTrackerViewSet(GenericViewSet):
    queryset = MilestoneTracker.objects.all()
    filterset_class = MilestoneTrackerFilter
    permission_classes = [HasGroupPermission]
    serializer_class = MilestoneTrackerSerializer

