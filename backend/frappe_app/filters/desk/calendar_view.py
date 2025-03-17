import django_filters as filters
from frappe_app.models.desk.calendar_view import CalendarView

class CalendarViewFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = CalendarView
        fields = ['id']

