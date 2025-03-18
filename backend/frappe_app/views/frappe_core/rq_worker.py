from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.rq_worker import RQWorker
from frappe_app.filters.frappe_core.rq_worker import RQWorkerFilter
from frappe_app.serializers.frappe_core.rq_worker import RQWorkerSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RQWorkerViewSet(GenericViewSet):
    queryset = RQWorker.objects.all()
    filterset_class = RQWorkerFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RQWorkerSerializer

