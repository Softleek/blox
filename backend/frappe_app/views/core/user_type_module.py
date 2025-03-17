from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.user_type_module import UserTypeModule
from frappe_app.filters.core.user_type_module import UserTypeModuleFilter
from frappe_app.serializers.core.user_type_module import UserTypeModuleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserTypeModuleViewSet(GenericViewSet):
    queryset = UserTypeModule.objects.all()
    filterset_class = UserTypeModuleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserTypeModuleSerializer

