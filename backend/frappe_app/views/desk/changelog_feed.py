from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.changelog_feed import ChangelogFeed
from frappe_app.filters.desk.changelog_feed import ChangelogFeedFilter
from frappe_app.serializers.desk.changelog_feed import ChangelogFeedSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ChangelogFeedViewSet(GenericViewSet):
    queryset = ChangelogFeed.objects.all()
    filterset_class = ChangelogFeedFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ChangelogFeedSerializer

