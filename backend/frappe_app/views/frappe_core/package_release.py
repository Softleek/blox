from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.package_release import PackageRelease
from frappe_app.filters.frappe_core.package_release import PackageReleaseFilter
from frappe_app.serializers.frappe_core.package_release import PackageReleaseSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PackageReleaseViewSet(GenericViewSet):
    queryset = PackageRelease.objects.all()
    filterset_class = PackageReleaseFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PackageReleaseSerializer

