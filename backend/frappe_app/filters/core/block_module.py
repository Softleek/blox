import django_filters as filters
from frappe_app.models.core.block_module import BlockModule

class BlockModuleFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = BlockModule
        fields = ['id']

