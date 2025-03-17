from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.help_article import HelpArticle
from frappe_app.filters.website.help_article import HelpArticleFilter
from frappe_app.serializers.website.help_article import HelpArticleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class HelpArticleViewSet(GenericViewSet):
    queryset = HelpArticle.objects.all()
    filterset_class = HelpArticleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = HelpArticleSerializer

