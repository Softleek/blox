from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.report import Report
from frappe_app.filters.frappe_core.report import ReportFilter
from frappe_app.serializers.frappe_core.report import ReportSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ReportViewSet(GenericViewSet):
    queryset = Report.objects.all()
    filterset_class = ReportFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ReportSerializer

