import django_filters as filters
from frappe_app.models.frappe_core.file import File

class FileFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = File
        fields = ['id']

