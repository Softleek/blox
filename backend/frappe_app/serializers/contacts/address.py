from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.contacts.address import Address

class AddressSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
