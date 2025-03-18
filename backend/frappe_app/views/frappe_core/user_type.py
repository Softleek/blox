from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.user_type import UserType
from frappe_app.filters.frappe_core.user_type import UserTypeFilter
from frappe_app.serializers.frappe_core.user_type import UserTypeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserTypeViewSet(GenericViewSet):
    queryset = UserType.objects.all()
    filterset_class = UserTypeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserTypeSerializer

