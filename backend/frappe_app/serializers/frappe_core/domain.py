from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.domain import Domain

class DomainSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = '__all__'
