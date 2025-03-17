from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.printing.print_heading import PrintHeading
from frappe_app.filters.printing.print_heading import PrintHeadingFilter
from frappe_app.serializers.printing.print_heading import PrintHeadingSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PrintHeadingViewSet(GenericViewSet):
    queryset = PrintHeading.objects.all()
    filterset_class = PrintHeadingFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PrintHeadingSerializer

