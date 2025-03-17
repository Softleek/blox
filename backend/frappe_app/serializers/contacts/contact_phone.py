from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.contacts.contact_phone import ContactPhone

class ContactPhoneSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ContactPhone
        fields = '__all__'
