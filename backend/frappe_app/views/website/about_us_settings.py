from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.about_us_settings import AboutUsSettings
from frappe_app.filters.website.about_us_settings import AboutUsSettingsFilter
from frappe_app.serializers.website.about_us_settings import AboutUsSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AboutUsSettingsViewSet(GenericViewSet):
    queryset = AboutUsSettings.objects.all()
    filterset_class = AboutUsSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AboutUsSettingsSerializer

