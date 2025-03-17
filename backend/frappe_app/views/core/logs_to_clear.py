from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.logs_to_clear import LogsToClear
from frappe_app.filters.core.logs_to_clear import LogsToClearFilter
from frappe_app.serializers.core.logs_to_clear import LogsToClearSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class LogsToClearViewSet(GenericViewSet):
    queryset = LogsToClear.objects.all()
    filterset_class = LogsToClearFilter
    permission_classes = [HasGroupPermission]
    serializer_class = LogsToClearSerializer

