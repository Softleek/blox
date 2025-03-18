from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.doctype import DocType
from frappe_app.filters.frappe_core.doctype import DocTypeFilter
from frappe_app.serializers.frappe_core.doctype import DocTypeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocTypeViewSet(GenericViewSet):
    queryset = DocType.objects.all()
    filterset_class = DocTypeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocTypeSerializer

