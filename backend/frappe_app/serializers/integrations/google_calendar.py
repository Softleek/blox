from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.google_calendar import GoogleCalendar

class GoogleCalendarSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = GoogleCalendar
        fields = '__all__'
