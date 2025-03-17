from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.utm_source import UTMSource

class UTMSourceSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UTMSource
        fields = '__all__'
