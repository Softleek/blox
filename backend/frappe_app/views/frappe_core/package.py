from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.package import Package
from frappe_app.filters.frappe_core.package import PackageFilter
from frappe_app.serializers.frappe_core.package import PackageSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PackageViewSet(GenericViewSet):
    queryset = Package.objects.all()
    filterset_class = PackageFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PackageSerializer

    filterset_class = PackageFilter
