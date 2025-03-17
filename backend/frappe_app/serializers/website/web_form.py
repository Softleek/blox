from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.web_form import WebForm

class WebFormSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebForm
        fields = '__all__'
