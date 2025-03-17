from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.utm_medium import UTMMedium

class UTMMediumSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UTMMedium
        fields = '__all__'
