from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.web_page_view import WebPageView

class WebPageViewSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebPageView
        fields = '__all__'
