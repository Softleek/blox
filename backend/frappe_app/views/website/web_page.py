from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.website.web_page import WebPage
from frappe_app.filters.website.web_page import WebPageFilter
from frappe_app.serializers.website.web_page import WebPageSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebPageViewSet(GenericViewSet):
    queryset = WebPage.objects.all()
    filterset_class = WebPageFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebPageSerializer

    filterset_class = WebPageFilter
