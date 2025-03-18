from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.rq_worker import RQWorker

class RQWorkerSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = RQWorker
        fields = '__all__'
