from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.top_bar_item import TopBarItem

class TopBarItemSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = TopBarItem
        fields = '__all__'
