import django_filters as filters
from frappe_app.models.website.contact_us_settings import ContactUsSettings

class ContactUsSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ContactUsSettings
        fields = ['id']

