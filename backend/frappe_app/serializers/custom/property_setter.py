from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.custom.property_setter import PropertySetter

class PropertySetterSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PropertySetter
        fields = '__all__'
