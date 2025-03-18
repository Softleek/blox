from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.transaction_log import TransactionLog

class TransactionLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = TransactionLog
        fields = '__all__'
