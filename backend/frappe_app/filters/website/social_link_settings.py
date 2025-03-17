import django_filters as filters
from frappe_app.models.website.social_link_settings import SocialLinkSettings

class SocialLinkSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SocialLinkSettings
        fields = ['id']

