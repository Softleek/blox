import django_filters as filters
from frappe_app.models.website.website_meta_tag import WebsiteMetaTag

class WebsiteMetaTagFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteMetaTag
        fields = ['id']

