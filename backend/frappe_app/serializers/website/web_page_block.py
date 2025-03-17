from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.web_page_block import WebPageBlock

class WebPageBlockSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebPageBlock
        fields = '__all__'
