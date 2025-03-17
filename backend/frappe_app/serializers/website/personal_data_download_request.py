from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.personal_data_download_request import PersonalDataDownloadRequest

class PersonalDataDownloadRequestSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PersonalDataDownloadRequest
        fields = '__all__'
