from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.number_card_link import NumberCardLink

class NumberCardLinkSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NumberCardLink
        fields = '__all__'
