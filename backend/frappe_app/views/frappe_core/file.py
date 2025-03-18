from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.file import File
from frappe_app.filters.frappe_core.file import FileFilter
from frappe_app.serializers.frappe_core.file import FileSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class FileViewSet(GenericViewSet):
    queryset = File.objects.all()
    filterset_class = FileFilter
    permission_classes = [HasGroupPermission]
    serializer_class = FileSerializer

