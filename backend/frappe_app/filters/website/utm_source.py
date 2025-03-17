import django_filters as filters
from frappe_app.models.website.utm_source import UTMSource

class UTMSourceFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UTMSource
        fields = ['id']

