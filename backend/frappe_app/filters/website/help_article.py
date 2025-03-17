import django_filters as filters
from frappe_app.models.website.help_article import HelpArticle

class HelpArticleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = HelpArticle
        fields = ['id']

