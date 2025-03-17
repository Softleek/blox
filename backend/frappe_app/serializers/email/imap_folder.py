from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.imap_folder import IMAPFolder

class IMAPFolderSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = IMAPFolder
        fields = '__all__'
