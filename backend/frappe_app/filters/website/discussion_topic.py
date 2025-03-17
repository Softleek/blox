import django_filters as filters
from frappe_app.models.website.discussion_topic import DiscussionTopic

class DiscussionTopicFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DiscussionTopic
        fields = ['id']

