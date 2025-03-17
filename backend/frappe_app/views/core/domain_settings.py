from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.domain_settings import DomainSettings
from frappe_app.filters.core.domain_settings import DomainSettingsFilter
from frappe_app.serializers.core.domain_settings import DomainSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DomainSettingsViewSet(GenericViewSet):
    queryset = DomainSettings.objects.all()
    filterset_class = DomainSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DomainSettingsSerializer

