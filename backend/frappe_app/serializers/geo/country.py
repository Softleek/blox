from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.geo.country import Country

class CountrySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'
