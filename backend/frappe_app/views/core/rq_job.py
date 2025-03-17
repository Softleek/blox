from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.rq_job import RQJob
from frappe_app.filters.core.rq_job import RQJobFilter
from frappe_app.serializers.core.rq_job import RQJobSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RQJobViewSet(GenericViewSet):
    queryset = RQJob.objects.all()
    filterset_class = RQJobFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RQJobSerializer

