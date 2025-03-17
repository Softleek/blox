import django_filters as filters
from frappe_app.models.printing.print_format import PrintFormat

class PrintFormatFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')
    doc_type = filters.CharFilter(lookup_expr='icontains', label='Doc Type')
    standard = filters.CharFilter(lookup_expr='icontains', label='Standard')

    class Meta:
        model = PrintFormat
        fields = ['id', 'doc_type', 'standard']

