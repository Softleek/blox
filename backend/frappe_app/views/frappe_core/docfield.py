from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.docfield import DocField
from frappe_app.filters.frappe_core.docfield import DocFieldFilter
from frappe_app.serializers.frappe_core.docfield import DocFieldSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocFieldViewSet(GenericViewSet):
    queryset = DocField.objects.all()
    filterset_class = DocFieldFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocFieldSerializer

