from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_route_redirect import WebsiteRouteRedirect

class WebsiteRouteRedirectSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteRouteRedirect
        fields = '__all__'
