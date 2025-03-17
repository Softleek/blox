import django_filters as filters
from frappe_app.models.desk.desktop_icon import DesktopIcon

class DesktopIconFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DesktopIcon
        fields = ['id']

