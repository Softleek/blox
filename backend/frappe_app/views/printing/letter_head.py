from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.printing.letter_head import LetterHead
from frappe_app.filters.printing.letter_head import LetterHeadFilter
from frappe_app.serializers.printing.letter_head import LetterHeadSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class LetterHeadViewSet(GenericViewSet):
    queryset = LetterHead.objects.all()
    filterset_class = LetterHeadFilter
    permission_classes = [HasGroupPermission]
    serializer_class = LetterHeadSerializer

