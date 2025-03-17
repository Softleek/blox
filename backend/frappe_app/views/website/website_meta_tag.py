from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_meta_tag import WebsiteMetaTag
from frappe_app.filters.website.website_meta_tag import WebsiteMetaTagFilter
from frappe_app.serializers.website.website_meta_tag import WebsiteMetaTagSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteMetaTagViewSet(GenericViewSet):
    queryset = WebsiteMetaTag.objects.all()
    filterset_class = WebsiteMetaTagFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteMetaTagSerializer

