from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.doctype_state import DocTypeState

class DocTypeStateSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocTypeState
        fields = '__all__'
