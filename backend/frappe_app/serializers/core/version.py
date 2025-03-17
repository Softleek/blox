from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.version import Version

class VersionSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = '__all__'
