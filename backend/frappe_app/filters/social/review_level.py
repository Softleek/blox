import django_filters as filters
from frappe_app.models.social.review_level import ReviewLevel

class ReviewLevelFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ReviewLevel
        fields = ['id']

