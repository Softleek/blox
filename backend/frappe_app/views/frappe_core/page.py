from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.page import Page
from frappe_app.filters.frappe_core.page import PageFilter
from frappe_app.serializers.frappe_core.page import PageSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PageViewSet(GenericViewSet):
    queryset = Page.objects.all()
    filterset_class = PageFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PageSerializer

