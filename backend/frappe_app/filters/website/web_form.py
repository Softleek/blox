import django_filters as filters
from frappe_app.models.website.web_form import WebForm

class WebFormFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebForm
        fields = ['id']

