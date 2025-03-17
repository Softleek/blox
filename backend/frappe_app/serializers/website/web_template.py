from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.web_template import WebTemplate

class WebTemplateSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebTemplate
        fields = '__all__'
