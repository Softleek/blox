from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.has_domain import HasDomain

class HasDomainSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = HasDomain
        fields = '__all__'
