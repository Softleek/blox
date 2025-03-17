from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.bulk_update import BulkUpdate

class BulkUpdateSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = BulkUpdate
        fields = '__all__'
