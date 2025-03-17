from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.rq_job import RQJob

class RQJobSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = RQJob
        fields = '__all__'
