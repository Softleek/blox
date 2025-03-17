from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.utm_campaign import UTMCampaign

class UTMCampaignSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UTMCampaign
        fields = '__all__'
