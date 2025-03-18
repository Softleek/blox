from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.role_profile import RoleProfile
from frappe_app.filters.frappe_core.role_profile import RoleProfileFilter
from frappe_app.serializers.frappe_core.role_profile import RoleProfileSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RoleProfileViewSet(GenericViewSet):
    queryset = RoleProfile.objects.all()
    filterset_class = RoleProfileFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RoleProfileSerializer

