from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.google_drive import GoogleDrive

class GoogleDriveSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = GoogleDrive
        fields = '__all__'
