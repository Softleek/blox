from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.amended_document_naming_settings import AmendedDocumentNamingSettings
from frappe_app.filters.frappe_core.amended_document_naming_settings import AmendedDocumentNamingSettingsFilter
from frappe_app.serializers.frappe_core.amended_document_naming_settings import AmendedDocumentNamingSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AmendedDocumentNamingSettingsViewSet(GenericViewSet):
    queryset = AmendedDocumentNamingSettings.objects.all()
    filterset_class = AmendedDocumentNamingSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AmendedDocumentNamingSettingsSerializer

