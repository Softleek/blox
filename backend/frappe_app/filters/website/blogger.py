import django_filters as filters
from frappe_app.models.website.blogger import Blogger

class BloggerFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Blogger
        fields = ['id']

