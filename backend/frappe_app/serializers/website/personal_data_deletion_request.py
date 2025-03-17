from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.personal_data_deletion_request import PersonalDataDeletionRequest

class PersonalDataDeletionRequestSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PersonalDataDeletionRequest
        fields = '__all__'
