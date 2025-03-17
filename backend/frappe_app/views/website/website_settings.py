from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_settings import WebsiteSettings
from frappe_app.filters.website.website_settings import WebsiteSettingsFilter
from frappe_app.serializers.website.website_settings import WebsiteSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteSettingsViewSet(GenericViewSet):
    queryset = WebsiteSettings.objects.all()
    filterset_class = WebsiteSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteSettingsSerializer

