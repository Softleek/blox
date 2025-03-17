from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.contacts.gender import Gender

class GenderSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = '__all__'
