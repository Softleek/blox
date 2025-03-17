import django_filters as filters
from frappe_app.models.website.discussion_reply import DiscussionReply

class DiscussionReplyFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DiscussionReply
        fields = ['id']

