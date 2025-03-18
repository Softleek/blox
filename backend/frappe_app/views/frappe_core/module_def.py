from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.module_def import ModuleDef
from frappe_app.filters.frappe_core.module_def import ModuleDefFilter
from frappe_app.serializers.frappe_core.module_def import ModuleDefSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ModuleDefViewSet(GenericViewSet):
    queryset = ModuleDef.objects.all()
    filterset_class = ModuleDefFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ModuleDefSerializer

