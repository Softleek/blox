from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.integrations.google_settings import GoogleSettings
from frappe_app.filters.integrations.google_settings import GoogleSettingsFilter
from frappe_app.serializers.integrations.google_settings import GoogleSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GoogleSettingsViewSet(SingleInstanceViewSet):
    queryset = GoogleSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = GoogleSettingsSerializer

    filterset_class = GoogleSettingsFilter
