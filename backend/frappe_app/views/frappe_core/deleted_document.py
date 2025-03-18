from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.deleted_document import DeletedDocument
from frappe_app.filters.frappe_core.deleted_document import DeletedDocumentFilter
from frappe_app.serializers.frappe_core.deleted_document import DeletedDocumentSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DeletedDocumentViewSet(GenericViewSet):
    queryset = DeletedDocument.objects.all()
    filterset_class = DeletedDocumentFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DeletedDocumentSerializer

