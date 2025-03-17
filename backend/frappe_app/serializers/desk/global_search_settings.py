from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.global_search_settings import GlobalSearchSettings

class GlobalSearchSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = GlobalSearchSettings
        fields = '__all__'
