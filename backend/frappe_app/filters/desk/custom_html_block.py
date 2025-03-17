import django_filters as filters
from frappe_app.models.desk.custom_html_block import CustomHTMLBlock

class CustomHTMLBlockFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = CustomHTMLBlock
        fields = ['id']

