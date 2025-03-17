from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.imap_folder import IMAPFolder
from frappe_app.filters.email.imap_folder import IMAPFolderFilter
from frappe_app.serializers.email.imap_folder import IMAPFolderSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class IMAPFolderViewSet(GenericViewSet):
    queryset = IMAPFolder.objects.all()
    filterset_class = IMAPFolderFilter
    permission_classes = [HasGroupPermission]
    serializer_class = IMAPFolderSerializer

