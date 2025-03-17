from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.list_filter import ListFilter

class ListFilterSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ListFilter
        fields = '__all__'
