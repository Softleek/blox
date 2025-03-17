from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.dropbox_settings import DropboxSettings
from frappe_app.filters.integrations.dropbox_settings import DropboxSettingsFilter
from frappe_app.serializers.integrations.dropbox_settings import DropboxSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DropboxSettingsViewSet(GenericViewSet):
    queryset = DropboxSettings.objects.all()
    filterset_class = DropboxSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DropboxSettingsSerializer

