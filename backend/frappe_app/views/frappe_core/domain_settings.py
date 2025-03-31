from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.domain_settings import DomainSettings
from frappe_app.filters.frappe_core.domain_settings import DomainSettingsFilter
from frappe_app.serializers.frappe_core.domain_settings import DomainSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DomainSettingsViewSet(SingleInstanceViewSet):
    queryset = DomainSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = DomainSettingsSerializer

    filterset_class = DomainSettingsFilter
