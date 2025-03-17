from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.document_share_key import DocumentShareKey
from frappe_app.filters.core.document_share_key import DocumentShareKeyFilter
from frappe_app.serializers.core.document_share_key import DocumentShareKeySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocumentShareKeyViewSet(GenericViewSet):
    queryset = DocumentShareKey.objects.all()
    filterset_class = DocumentShareKeyFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocumentShareKeySerializer

