from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.custom.doctype_layout_field import DocTypeLayoutField
from frappe_app.filters.custom.doctype_layout_field import DocTypeLayoutFieldFilter
from frappe_app.serializers.custom.doctype_layout_field import DocTypeLayoutFieldSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocTypeLayoutFieldViewSet(GenericViewSet):
    queryset = DocTypeLayoutField.objects.all()
    filterset_class = DocTypeLayoutFieldFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocTypeLayoutFieldSerializer

