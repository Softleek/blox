from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.comment import Comment
from frappe_app.filters.frappe_core.comment import CommentFilter
from frappe_app.serializers.frappe_core.comment import CommentSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CommentViewSet(GenericViewSet):
    queryset = Comment.objects.all()
    filterset_class = CommentFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CommentSerializer

