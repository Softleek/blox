import django_filters as filters
from frappe_app.models.website.web_page_block import WebPageBlock

class WebPageBlockFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebPageBlock
        fields = ['id']

