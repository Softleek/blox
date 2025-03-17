import django_filters as filters
from frappe_app.models.website.blog_post import BlogPost

class BlogPostFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = BlogPost
        fields = ['id']

