from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.printing.print_style import PrintStyle
from frappe_app.filters.printing.print_style import PrintStyleFilter
from frappe_app.serializers.printing.print_style import PrintStyleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PrintStyleViewSet(GenericViewSet):
    queryset = PrintStyle.objects.all()
    filterset_class = PrintStyleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PrintStyleSerializer

