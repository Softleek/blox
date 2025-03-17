from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.automation.auto_repeat import AutoRepeat
from frappe_app.filters.automation.auto_repeat import AutoRepeatFilter
from frappe_app.serializers.automation.auto_repeat import AutoRepeatSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AutoRepeatViewSet(GenericViewSet):
    queryset = AutoRepeat.objects.all()
    filterset_class = AutoRepeatFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AutoRepeatSerializer

