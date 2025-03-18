from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.data_export import DataExport
from frappe_app.filters.frappe_core.data_export import DataExportFilter
from frappe_app.serializers.frappe_core.data_export import DataExportSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DataExportViewSet(GenericViewSet):
    queryset = DataExport.objects.all()
    filterset_class = DataExportFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DataExportSerializer

