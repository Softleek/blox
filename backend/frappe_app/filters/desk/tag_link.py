import django_filters as filters
from frappe_app.models.desk.tag_link import TagLink

class TagLinkFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = TagLink
        fields = ['id']

