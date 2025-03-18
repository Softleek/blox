from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.report_column import ReportColumn
from frappe_app.filters.frappe_core.report_column import ReportColumnFilter
from frappe_app.serializers.frappe_core.report_column import ReportColumnSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ReportColumnViewSet(GenericViewSet):
    queryset = ReportColumn.objects.all()
    filterset_class = ReportColumnFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ReportColumnSerializer

