from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_theme_ignore_app import WebsiteThemeIgnoreApp
from frappe_app.filters.website.website_theme_ignore_app import WebsiteThemeIgnoreAppFilter
from frappe_app.serializers.website.website_theme_ignore_app import WebsiteThemeIgnoreAppSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteThemeIgnoreAppViewSet(GenericViewSet):
    queryset = WebsiteThemeIgnoreApp.objects.all()
    filterset_class = WebsiteThemeIgnoreAppFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteThemeIgnoreAppSerializer

