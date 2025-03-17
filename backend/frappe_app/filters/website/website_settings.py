import django_filters as filters
from frappe_app.models.website.website_settings import WebsiteSettings

class WebsiteSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteSettings
        fields = ['id']

