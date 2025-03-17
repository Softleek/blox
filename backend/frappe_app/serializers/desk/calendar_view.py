from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.calendar_view import CalendarView

class CalendarViewSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = CalendarView
        fields = '__all__'
