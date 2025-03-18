from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.submission_queue import SubmissionQueue

class SubmissionQueueSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SubmissionQueue
        fields = '__all__'
