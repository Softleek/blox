from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.personal_data_deletion_step import PersonalDataDeletionStep

class PersonalDataDeletionStepSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PersonalDataDeletionStep
        fields = '__all__'
