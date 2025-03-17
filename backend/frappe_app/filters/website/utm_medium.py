import django_filters as filters
from frappe_app.models.website.utm_medium import UTMMedium

class UTMMediumFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UTMMedium
        fields = ['id']

