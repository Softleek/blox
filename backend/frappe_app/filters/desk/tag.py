import django_filters as filters
from frappe_app.models.desk.tag import Tag

class TagFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Tag
        fields = ['id']

