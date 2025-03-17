from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.docshare import DocShare
from frappe_app.filters.core.docshare import DocShareFilter
from frappe_app.serializers.core.docshare import DocShareSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocShareViewSet(GenericViewSet):
    queryset = DocShare.objects.all()
    filterset_class = DocShareFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocShareSerializer

