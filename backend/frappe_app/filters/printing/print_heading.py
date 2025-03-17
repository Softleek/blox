import django_filters as filters
from frappe_app.models.printing.print_heading import PrintHeading

class PrintHeadingFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')
    print_heading = filters.CharFilter(lookup_expr='icontains', label='Print Heading')

    class Meta:
        model = PrintHeading
        fields = ['id', 'print_heading']

