from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.page import Page

class PageSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = '__all__'
