from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_slideshow import WebsiteSlideshow
from frappe_app.filters.website.website_slideshow import WebsiteSlideshowFilter
from frappe_app.serializers.website.website_slideshow import WebsiteSlideshowSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteSlideshowViewSet(GenericViewSet):
    queryset = WebsiteSlideshow.objects.all()
    filterset_class = WebsiteSlideshowFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteSlideshowSerializer

