from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.data_import import DataImport
from frappe_app.filters.frappe_core.data_import import DataImportFilter
from frappe_app.serializers.frappe_core.data_import import DataImportSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DataImportViewSet(GenericViewSet):
    queryset = DataImport.objects.all()
    filterset_class = DataImportFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DataImportSerializer

