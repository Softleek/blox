from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.automation.milestone import Milestone
from frappe_app.filters.automation.milestone import MilestoneFilter
from frappe_app.serializers.automation.milestone import MilestoneSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class MilestoneViewSet(GenericViewSet):
    queryset = Milestone.objects.all()
    filterset_class = MilestoneFilter
    permission_classes = [HasGroupPermission]
    serializer_class = MilestoneSerializer

