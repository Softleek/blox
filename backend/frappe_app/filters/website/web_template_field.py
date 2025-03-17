import django_filters as filters
from frappe_app.models.website.web_template_field import WebTemplateField

class WebTemplateFieldFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebTemplateField
        fields = ['id']

