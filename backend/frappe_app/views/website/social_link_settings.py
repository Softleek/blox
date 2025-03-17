from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.social_link_settings import SocialLinkSettings
from frappe_app.filters.website.social_link_settings import SocialLinkSettingsFilter
from frappe_app.serializers.website.social_link_settings import SocialLinkSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SocialLinkSettingsViewSet(GenericViewSet):
    queryset = SocialLinkSettings.objects.all()
    filterset_class = SocialLinkSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SocialLinkSettingsSerializer

