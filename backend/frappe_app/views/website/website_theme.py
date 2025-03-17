from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_theme import WebsiteTheme
from frappe_app.filters.website.website_theme import WebsiteThemeFilter
from frappe_app.serializers.website.website_theme import WebsiteThemeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteThemeViewSet(GenericViewSet):
    queryset = WebsiteTheme.objects.all()
    filterset_class = WebsiteThemeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteThemeSerializer

