from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.desktop_icon import DesktopIcon

class DesktopIconSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DesktopIcon
        fields = '__all__'
