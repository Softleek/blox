from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.web_form_list_column import WebFormListColumn

class WebFormListColumnSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebFormListColumn
        fields = '__all__'
