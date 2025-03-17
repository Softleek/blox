from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.log_setting_user import LogSettingUser

class LogSettingUserSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = LogSettingUser
        fields = '__all__'
