from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.file import File

class FileSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'
