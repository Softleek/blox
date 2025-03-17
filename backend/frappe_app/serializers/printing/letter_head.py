from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.printing.letter_head import LetterHead

class LetterHeadSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = LetterHead
        fields = '__all__'
