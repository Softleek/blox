import django_filters as filters
from frappe_app.models.frappe_core.role_permission_for_page_and_report import RolePermissionForPageAndReport

class RolePermissionForPageAndReportFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = RolePermissionForPageAndReport
        fields = ['id']

