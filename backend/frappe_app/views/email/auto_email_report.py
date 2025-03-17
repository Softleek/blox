from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.auto_email_report import AutoEmailReport
from frappe_app.filters.email.auto_email_report import AutoEmailReportFilter
from frappe_app.serializers.email.auto_email_report import AutoEmailReportSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AutoEmailReportViewSet(GenericViewSet):
    queryset = AutoEmailReport.objects.all()
    filterset_class = AutoEmailReportFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AutoEmailReportSerializer

