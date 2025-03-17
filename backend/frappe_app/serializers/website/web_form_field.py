from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.web_form_field import WebFormField

class WebFormFieldSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebFormField
        fields = '__all__'
