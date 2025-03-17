import django_filters as filters
from frappe_app.models.printing.print_format_field_template import PrintFormatFieldTemplate

class PrintFormatFieldTemplateFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PrintFormatFieldTemplate
        fields = ['id']

