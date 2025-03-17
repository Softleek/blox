from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.user_document_type import UserDocumentType
from frappe_app.filters.core.user_document_type import UserDocumentTypeFilter
from frappe_app.serializers.core.user_document_type import UserDocumentTypeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserDocumentTypeViewSet(GenericViewSet):
    queryset = UserDocumentType.objects.all()
    filterset_class = UserDocumentTypeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserDocumentTypeSerializer

