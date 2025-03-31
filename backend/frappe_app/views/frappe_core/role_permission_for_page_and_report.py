from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.role_permission_for_page_and_report import RolePermissionForPageAndReport
from frappe_app.filters.frappe_core.role_permission_for_page_and_report import RolePermissionForPageAndReportFilter
from frappe_app.serializers.frappe_core.role_permission_for_page_and_report import RolePermissionForPageAndReportSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RolePermissionForPageAndReportViewSet(SingleInstanceViewSet):
    queryset = RolePermissionForPageAndReport.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = RolePermissionForPageAndReportSerializer

    filterset_class = RolePermissionForPageAndReportFilter
