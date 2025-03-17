from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.patch_log import PatchLog

class PatchLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PatchLog
        fields = '__all__'
