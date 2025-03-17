from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.doctype_action import DocTypeAction

class DocTypeActionSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocTypeAction
        fields = '__all__'
