from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.geo.currency import Currency

class CurrencySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'
