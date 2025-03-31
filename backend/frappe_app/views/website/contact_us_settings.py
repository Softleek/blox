from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.website.contact_us_settings import ContactUsSettings
from frappe_app.filters.website.contact_us_settings import ContactUsSettingsFilter
from frappe_app.serializers.website.contact_us_settings import ContactUsSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ContactUsSettingsViewSet(SingleInstanceViewSet):
    queryset = ContactUsSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = ContactUsSettingsSerializer

    filterset_class = ContactUsSettingsFilter
