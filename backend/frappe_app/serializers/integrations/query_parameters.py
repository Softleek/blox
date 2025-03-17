from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.query_parameters import QueryParameters

class QueryParametersSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = QueryParameters
        fields = '__all__'
