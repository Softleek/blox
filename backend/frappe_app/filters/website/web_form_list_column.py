import django_filters as filters
from frappe_app.models.website.web_form_list_column import WebFormListColumn

class WebFormListColumnFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebFormListColumn
        fields = ['id']

