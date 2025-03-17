from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_slideshow_item import WebsiteSlideshowItem
from frappe_app.filters.website.website_slideshow_item import WebsiteSlideshowItemFilter
from frappe_app.serializers.website.website_slideshow_item import WebsiteSlideshowItemSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteSlideshowItemViewSet(GenericViewSet):
    queryset = WebsiteSlideshowItem.objects.all()
    filterset_class = WebsiteSlideshowItemFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteSlideshowItemSerializer

