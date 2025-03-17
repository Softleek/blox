from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.contacts.contact import Contact

class ContactSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
