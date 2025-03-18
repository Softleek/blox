from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.doctype_link import DocTypeLink
from frappe_app.filters.frappe_core.doctype_link import DocTypeLinkFilter
from frappe_app.serializers.frappe_core.doctype_link import DocTypeLinkSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocTypeLinkViewSet(GenericViewSet):
    queryset = DocTypeLink.objects.all()
    filterset_class = DocTypeLinkFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocTypeLinkSerializer

