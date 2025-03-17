from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.web_page_view import WebPageView
from frappe_app.filters.website.web_page_view import WebPageViewFilter
from frappe_app.serializers.website.web_page_view import WebPageViewSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebPageViewViewSet(GenericViewSet):
    queryset = WebPageView.objects.all()
    filterset_class = WebPageViewFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebPageViewSerializer

