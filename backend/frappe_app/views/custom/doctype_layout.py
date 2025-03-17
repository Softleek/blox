from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.custom.doctype_layout import DocTypeLayout
from frappe_app.filters.custom.doctype_layout import DocTypeLayoutFilter
from frappe_app.serializers.custom.doctype_layout import DocTypeLayoutSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocTypeLayoutViewSet(GenericViewSet):
    queryset = DocTypeLayout.objects.all()
    filterset_class = DocTypeLayoutFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocTypeLayoutSerializer

