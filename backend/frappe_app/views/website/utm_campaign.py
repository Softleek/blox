from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.utm_campaign import UTMCampaign
from frappe_app.filters.website.utm_campaign import UTMCampaignFilter
from frappe_app.serializers.website.utm_campaign import UTMCampaignSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UTMCampaignViewSet(GenericViewSet):
    queryset = UTMCampaign.objects.all()
    filterset_class = UTMCampaignFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UTMCampaignSerializer

