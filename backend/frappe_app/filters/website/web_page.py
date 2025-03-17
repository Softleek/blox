import django_filters as filters
from frappe_app.models.website.web_page import WebPage

class WebPageFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebPage
        fields = ['id']

