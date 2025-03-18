from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.user_role_profile import UserRoleProfile
from frappe_app.filters.frappe_core.user_role_profile import UserRoleProfileFilter
from frappe_app.serializers.frappe_core.user_role_profile import UserRoleProfileSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserRoleProfileViewSet(GenericViewSet):
    queryset = UserRoleProfile.objects.all()
    filterset_class = UserRoleProfileFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserRoleProfileSerializer

