from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.navbar_settings import NavbarSettings
from frappe_app.filters.core.navbar_settings import NavbarSettingsFilter
from frappe_app.serializers.core.navbar_settings import NavbarSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NavbarSettingsViewSet(GenericViewSet):
    queryset = NavbarSettings.objects.all()
    filterset_class = NavbarSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NavbarSettingsSerializer

