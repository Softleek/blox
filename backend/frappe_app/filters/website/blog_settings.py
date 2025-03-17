import django_filters as filters
from frappe_app.models.website.blog_settings import BlogSettings

class BlogSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = BlogSettings
        fields = ['id']

