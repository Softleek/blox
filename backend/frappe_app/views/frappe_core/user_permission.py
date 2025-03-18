from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.user_permission import UserPermission
from frappe_app.filters.frappe_core.user_permission import UserPermissionFilter
from frappe_app.serializers.frappe_core.user_permission import UserPermissionSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserPermissionViewSet(GenericViewSet):
    queryset = UserPermission.objects.all()
    filterset_class = UserPermissionFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserPermissionSerializer

