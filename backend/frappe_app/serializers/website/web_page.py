from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.web_page import WebPage

class WebPageSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebPage
        fields = '__all__'
