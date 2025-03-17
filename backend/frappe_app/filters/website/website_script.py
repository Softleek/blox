import django_filters as filters
from frappe_app.models.website.website_script import WebsiteScript

class WebsiteScriptFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteScript
        fields = ['id']

