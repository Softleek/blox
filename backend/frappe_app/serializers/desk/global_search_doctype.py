from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.global_search_doctype import GlobalSearchDocType

class GlobalSearchDocTypeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = GlobalSearchDocType
        fields = '__all__'
