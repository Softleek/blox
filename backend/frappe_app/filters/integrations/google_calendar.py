import django_filters as filters
from frappe_app.models.integrations.google_calendar import GoogleCalendar

class GoogleCalendarFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = GoogleCalendar
        fields = ['id']

