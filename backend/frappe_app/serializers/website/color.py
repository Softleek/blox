from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.color import Color

class ColorSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'
