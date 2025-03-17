from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.google_contacts import GoogleContacts

class GoogleContactsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = GoogleContacts
        fields = '__all__'
