from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_route_meta import WebsiteRouteMeta

class WebsiteRouteMetaSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteRouteMeta
        fields = '__all__'
