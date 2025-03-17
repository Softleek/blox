from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_meta_tag import WebsiteMetaTag

class WebsiteMetaTagSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteMetaTag
        fields = '__all__'
