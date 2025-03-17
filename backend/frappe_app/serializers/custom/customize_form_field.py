from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.custom.customize_form_field import CustomizeFormField

class CustomizeFormFieldSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = CustomizeFormField
        fields = '__all__'
