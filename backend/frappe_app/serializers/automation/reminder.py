from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.automation.reminder import Reminder

class ReminderSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = '__all__'
