import django_filters as filters
from frappe_app.models.website.blog_category import BlogCategory

class BlogCategoryFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = BlogCategory
        fields = ['id']

