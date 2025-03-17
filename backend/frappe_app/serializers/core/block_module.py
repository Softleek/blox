from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.block_module import BlockModule

class BlockModuleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = BlockModule
        fields = '__all__'
