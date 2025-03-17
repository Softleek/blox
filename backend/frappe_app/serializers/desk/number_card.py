from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.number_card import NumberCard

class NumberCardSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NumberCard
        fields = '__all__'
