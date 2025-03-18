from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.translation import Translation

class TranslationSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Translation
        fields = '__all__'
