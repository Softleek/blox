import django_filters as filters
from frappe_app.models.printing.letter_head import LetterHead

class LetterHeadFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = LetterHead
        fields = ['id']

