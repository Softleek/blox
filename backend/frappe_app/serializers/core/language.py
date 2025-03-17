from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.language import Language

class LanguageSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'
