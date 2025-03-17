from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.company_history import CompanyHistory

class CompanyHistorySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = CompanyHistory
        fields = '__all__'
