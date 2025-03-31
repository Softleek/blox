from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.website.website_settings import WebsiteSettings
from frappe_app.filters.website.website_settings import WebsiteSettingsFilter
from frappe_app.serializers.website.website_settings import WebsiteSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteSettingsViewSet(SingleInstanceViewSet):
    queryset = WebsiteSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteSettingsSerializer

    filterset_class = WebsiteSettingsFilter
