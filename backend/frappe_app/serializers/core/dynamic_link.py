from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.dynamic_link import DynamicLink

class DynamicLinkSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DynamicLink
        fields = '__all__'
