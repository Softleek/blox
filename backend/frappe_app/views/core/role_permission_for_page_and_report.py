from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.role_permission_for_page_and_report import RolePermissionForPageAndReport
from frappe_app.filters.core.role_permission_for_page_and_report import RolePermissionForPageAndReportFilter
from frappe_app.serializers.core.role_permission_for_page_and_report import RolePermissionForPageAndReportSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RolePermissionForPageAndReportViewSet(GenericViewSet):
    queryset = RolePermissionForPageAndReport.objects.all()
    filterset_class = RolePermissionForPageAndReportFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RolePermissionForPageAndReportSerializer

