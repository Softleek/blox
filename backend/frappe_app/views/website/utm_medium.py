from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.utm_medium import UTMMedium
from frappe_app.filters.website.utm_medium import UTMMediumFilter
from frappe_app.serializers.website.utm_medium import UTMMediumSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UTMMediumViewSet(GenericViewSet):
    queryset = UTMMedium.objects.all()
    filterset_class = UTMMediumFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UTMMediumSerializer

