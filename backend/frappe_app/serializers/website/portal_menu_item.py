from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.portal_menu_item import PortalMenuItem

class PortalMenuItemSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PortalMenuItem
        fields = '__all__'
