from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.block_module import BlockModule
from frappe_app.filters.frappe_core.block_module import BlockModuleFilter
from frappe_app.serializers.frappe_core.block_module import BlockModuleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class BlockModuleViewSet(GenericViewSet):
    queryset = BlockModule.objects.all()
    filterset_class = BlockModuleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = BlockModuleSerializer

