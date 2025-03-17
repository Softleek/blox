from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.contacts.contact_email import ContactEmail

class ContactEmailSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ContactEmail
        fields = '__all__'
