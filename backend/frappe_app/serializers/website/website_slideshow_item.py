from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_slideshow_item import WebsiteSlideshowItem

class WebsiteSlideshowItemSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteSlideshowItem
        fields = '__all__'
