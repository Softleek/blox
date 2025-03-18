from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.module_profile import ModuleProfile
from frappe_app.filters.frappe_core.module_profile import ModuleProfileFilter
from frappe_app.serializers.frappe_core.module_profile import ModuleProfileSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ModuleProfileViewSet(GenericViewSet):
    queryset = ModuleProfile.objects.all()
    filterset_class = ModuleProfileFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ModuleProfileSerializer

