from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.custom.customize_form import CustomizeForm

class CustomizeFormSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = CustomizeForm
        fields = '__all__'
