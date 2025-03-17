from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_slideshow import WebsiteSlideshow

class WebsiteSlideshowSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteSlideshow
        fields = '__all__'
