import django_filters as filters
from frappe_app.models.website.utm_campaign import UTMCampaign

class UTMCampaignFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')
    campaign_description = filters.CharFilter(lookup_expr='icontains', label='Campaign Description')

    class Meta:
        model = UTMCampaign
        fields = ['id', 'campaign_description']

