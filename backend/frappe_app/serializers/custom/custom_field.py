from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.custom.custom_field import CustomField

class CustomFieldSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = CustomField
        fields = '__all__'
