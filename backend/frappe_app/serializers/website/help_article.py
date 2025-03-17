from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.help_article import HelpArticle

class HelpArticleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = HelpArticle
        fields = '__all__'
