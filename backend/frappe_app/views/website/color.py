from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.color import Color
from frappe_app.filters.website.color import ColorFilter
from frappe_app.serializers.website.color import ColorSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ColorViewSet(GenericViewSet):
    queryset = Color.objects.all()
    filterset_class = ColorFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ColorSerializer

