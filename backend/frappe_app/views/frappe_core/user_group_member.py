from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.user_group_member import UserGroupMember
from frappe_app.filters.frappe_core.user_group_member import UserGroupMemberFilter
from frappe_app.serializers.frappe_core.user_group_member import UserGroupMemberSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserGroupMemberViewSet(GenericViewSet):
    queryset = UserGroupMember.objects.all()
    filterset_class = UserGroupMemberFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserGroupMemberSerializer

