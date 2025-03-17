from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.report_filter import ReportFilter
from frappe_app.filters.core.report_filter import ReportFilterFilter
from frappe_app.serializers.core.report_filter import ReportFilterSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ReportFilterViewSet(GenericViewSet):
    queryset = ReportFilter.objects.all()
    filterset_class = ReportFilterFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ReportFilterSerializer

