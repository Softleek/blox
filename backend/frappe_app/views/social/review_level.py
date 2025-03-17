from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.social.review_level import ReviewLevel
from frappe_app.filters.social.review_level import ReviewLevelFilter
from frappe_app.serializers.social.review_level import ReviewLevelSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ReviewLevelViewSet(GenericViewSet):
    queryset = ReviewLevel.objects.all()
    filterset_class = ReviewLevelFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ReviewLevelSerializer

