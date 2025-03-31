from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.website.about_us_settings import AboutUsSettings
from frappe_app.filters.website.about_us_settings import AboutUsSettingsFilter
from frappe_app.serializers.website.about_us_settings import AboutUsSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AboutUsSettingsViewSet(SingleInstanceViewSet):
    queryset = AboutUsSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = AboutUsSettingsSerializer

    filterset_class = AboutUsSettingsFilter
