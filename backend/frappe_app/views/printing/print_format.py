from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.printing.print_format import PrintFormat
from frappe_app.filters.printing.print_format import PrintFormatFilter
from frappe_app.serializers.printing.print_format import PrintFormatSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PrintFormatViewSet(GenericViewSet):
    queryset = PrintFormat.objects.all()
    filterset_class = PrintFormatFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PrintFormatSerializer

