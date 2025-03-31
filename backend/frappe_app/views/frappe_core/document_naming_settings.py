from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.document_naming_settings import DocumentNamingSettings
from frappe_app.filters.frappe_core.document_naming_settings import DocumentNamingSettingsFilter
from frappe_app.serializers.frappe_core.document_naming_settings import DocumentNamingSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocumentNamingSettingsViewSet(SingleInstanceViewSet):
    queryset = DocumentNamingSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = DocumentNamingSettingsSerializer

    filterset_class = DocumentNamingSettingsFilter
