from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_sidebar_item import WebsiteSidebarItem

class WebsiteSidebarItemSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteSidebarItem
        fields = '__all__'
