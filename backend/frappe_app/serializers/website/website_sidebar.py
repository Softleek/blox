from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_sidebar import WebsiteSidebar

class WebsiteSidebarSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteSidebar
        fields = '__all__'
