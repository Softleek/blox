import django_filters as filters
from frappe_app.models.desk.changelog_feed import ChangelogFeed

class ChangelogFeedFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ChangelogFeed
        fields = ['id']

