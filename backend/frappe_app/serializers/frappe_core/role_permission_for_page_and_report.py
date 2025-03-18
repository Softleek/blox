from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.role_permission_for_page_and_report import RolePermissionForPageAndReport

class RolePermissionForPageAndReportSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = RolePermissionForPageAndReport
        fields = '__all__'
