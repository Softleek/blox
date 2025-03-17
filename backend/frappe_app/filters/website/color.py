import django_filters as filters
from frappe_app.models.website.color import Color

class ColorFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Color
        fields = ['id']

