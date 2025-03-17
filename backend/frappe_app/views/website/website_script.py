from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_script import WebsiteScript
from frappe_app.filters.website.website_script import WebsiteScriptFilter
from frappe_app.serializers.website.website_script import WebsiteScriptSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteScriptViewSet(GenericViewSet):
    queryset = WebsiteScript.objects.all()
    filterset_class = WebsiteScriptFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteScriptSerializer

