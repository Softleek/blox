from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.success_action import SuccessAction

class SuccessActionSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SuccessAction
        fields = '__all__'
