from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.contacts.address_template import AddressTemplate

class AddressTemplateSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AddressTemplate
        fields = '__all__'
