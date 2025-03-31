from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.navbar_settings import NavbarSettings
from frappe_app.filters.frappe_core.navbar_settings import NavbarSettingsFilter
from frappe_app.serializers.frappe_core.navbar_settings import NavbarSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NavbarSettingsViewSet(SingleInstanceViewSet):
    queryset = NavbarSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = NavbarSettingsSerializer

    filterset_class = NavbarSettingsFilter
