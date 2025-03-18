from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.recorder import Recorder
from frappe_app.filters.frappe_core.recorder import RecorderFilter
from frappe_app.serializers.frappe_core.recorder import RecorderSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RecorderViewSet(GenericViewSet):
    queryset = Recorder.objects.all()
    filterset_class = RecorderFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RecorderSerializer

