from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.custom_docperm import CustomDocPerm

class CustomDocPermSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = CustomDocPerm
        fields = '__all__'
