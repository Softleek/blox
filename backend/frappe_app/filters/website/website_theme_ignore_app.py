import django_filters as filters
from frappe_app.models.website.website_theme_ignore_app import WebsiteThemeIgnoreApp

class WebsiteThemeIgnoreAppFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteThemeIgnoreApp
        fields = ['id']

