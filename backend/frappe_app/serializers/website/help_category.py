from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.help_category import HelpCategory

class HelpCategorySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = HelpCategory
        fields = '__all__'
