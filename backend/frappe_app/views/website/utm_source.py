from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.utm_source import UTMSource
from frappe_app.filters.website.utm_source import UTMSourceFilter
from frappe_app.serializers.website.utm_source import UTMSourceSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UTMSourceViewSet(GenericViewSet):
    queryset = UTMSource.objects.all()
    filterset_class = UTMSourceFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UTMSourceSerializer

