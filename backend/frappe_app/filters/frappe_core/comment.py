import django_filters as filters
from frappe_app.models.frappe_core.comment import Comment

class CommentFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Comment
        fields = ['id']

