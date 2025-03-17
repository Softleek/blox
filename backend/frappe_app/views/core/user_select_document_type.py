from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.user_select_document_type import UserSelectDocumentType
from frappe_app.filters.core.user_select_document_type import UserSelectDocumentTypeFilter
from frappe_app.serializers.core.user_select_document_type import UserSelectDocumentTypeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserSelectDocumentTypeViewSet(GenericViewSet):
    queryset = UserSelectDocumentType.objects.all()
    filterset_class = UserSelectDocumentTypeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserSelectDocumentTypeSerializer

