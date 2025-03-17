import django_filters as filters
from frappe_app.models.printing.print_style import PrintStyle

class PrintStyleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PrintStyle
        fields = ['id']

