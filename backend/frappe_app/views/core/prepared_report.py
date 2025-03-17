from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.prepared_report import PreparedReport
from frappe_app.filters.core.prepared_report import PreparedReportFilter
from frappe_app.serializers.core.prepared_report import PreparedReportSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PreparedReportViewSet(GenericViewSet):
    queryset = PreparedReport.objects.all()
    filterset_class = PreparedReportFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PreparedReportSerializer

