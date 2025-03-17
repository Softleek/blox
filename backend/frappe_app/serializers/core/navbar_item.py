from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.navbar_item import NavbarItem

class NavbarItemSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NavbarItem
        fields = '__all__'
