from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.package_import import PackageImport
from frappe_app.filters.core.package_import import PackageImportFilter
from frappe_app.serializers.core.package_import import PackageImportSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PackageImportViewSet(GenericViewSet):
    queryset = PackageImport.objects.all()
    filterset_class = PackageImportFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PackageImportSerializer

