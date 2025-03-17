from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.user_group import UserGroup
from frappe_app.filters.core.user_group import UserGroupFilter
from frappe_app.serializers.core.user_group import UserGroupSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserGroupViewSet(GenericViewSet):
    queryset = UserGroup.objects.all()
    filterset_class = UserGroupFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserGroupSerializer

