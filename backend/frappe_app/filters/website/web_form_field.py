import django_filters as filters
from frappe_app.models.website.web_form_field import WebFormField

class WebFormFieldFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebFormField
        fields = ['id']

