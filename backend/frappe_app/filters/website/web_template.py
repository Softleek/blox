import django_filters as filters
from frappe_app.models.website.web_template import WebTemplate

class WebTemplateFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebTemplate
        fields = ['id']

