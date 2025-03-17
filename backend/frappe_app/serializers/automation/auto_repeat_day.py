from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.automation.auto_repeat_day import AutoRepeatDay

class AutoRepeatDaySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AutoRepeatDay
        fields = '__all__'
