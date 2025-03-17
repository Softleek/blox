import django_filters as filters
from frappe_app.models.automation.reminder import Reminder

class ReminderFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Reminder
        fields = ['id']

