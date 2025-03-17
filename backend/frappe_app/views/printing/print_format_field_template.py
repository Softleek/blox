from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.printing.print_format_field_template import PrintFormatFieldTemplate
from frappe_app.filters.printing.print_format_field_template import PrintFormatFieldTemplateFilter
from frappe_app.serializers.printing.print_format_field_template import PrintFormatFieldTemplateSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PrintFormatFieldTemplateViewSet(GenericViewSet):
    queryset = PrintFormatFieldTemplate.objects.all()
    filterset_class = PrintFormatFieldTemplateFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PrintFormatFieldTemplateSerializer

