from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.dynamic_link import DynamicLink
from frappe_app.filters.frappe_core.dynamic_link import DynamicLinkFilter
from frappe_app.serializers.frappe_core.dynamic_link import DynamicLinkSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DynamicLinkViewSet(GenericViewSet):
    queryset = DynamicLink.objects.all()
    filterset_class = DynamicLinkFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DynamicLinkSerializer

