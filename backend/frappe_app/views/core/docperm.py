from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.docperm import DocPerm
from frappe_app.filters.core.docperm import DocPermFilter
from frappe_app.serializers.core.docperm import DocPermSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocPermViewSet(GenericViewSet):
    queryset = DocPerm.objects.all()
    filterset_class = DocPermFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocPermSerializer

