from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.data_import_log import DataImportLog
from frappe_app.filters.core.data_import_log import DataImportLogFilter
from frappe_app.serializers.core.data_import_log import DataImportLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DataImportLogViewSet(GenericViewSet):
    queryset = DataImportLog.objects.all()
    filterset_class = DataImportLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DataImportLogSerializer

