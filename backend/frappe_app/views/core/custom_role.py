from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.custom_role import CustomRole
from frappe_app.filters.core.custom_role import CustomRoleFilter
from frappe_app.serializers.core.custom_role import CustomRoleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CustomRoleViewSet(GenericViewSet):
    queryset = CustomRole.objects.all()
    filterset_class = CustomRoleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CustomRoleSerializer

