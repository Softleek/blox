import django_filters as filters
from frappe_app.models.website.about_us_settings import AboutUsSettings

class AboutUsSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AboutUsSettings
        fields = ['id']

