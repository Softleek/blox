from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.docshare import DocShare
from frappe_app.filters.frappe_core.docshare import DocShareFilter
from frappe_app.serializers.frappe_core.docshare import DocShareSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocShareViewSet(GenericViewSet):
    queryset = DocShare.objects.all()
    filterset_class = DocShareFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocShareSerializer

    filterset_class = DocShareFilter
