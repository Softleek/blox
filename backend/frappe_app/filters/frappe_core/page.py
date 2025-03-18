import django_filters as filters
from frappe_app.models.frappe_core.page import Page

class PageFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Page
        fields = ['id']

