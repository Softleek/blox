from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.contacts.salutation import Salutation

class SalutationSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Salutation
        fields = '__all__'
