from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.web_template_field import WebTemplateField

class WebTemplateFieldSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebTemplateField
        fields = '__all__'
