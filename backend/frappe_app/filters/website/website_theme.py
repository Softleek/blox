import django_filters as filters
from frappe_app.models.website.website_theme import WebsiteTheme

class WebsiteThemeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteTheme
        fields = ['id']

