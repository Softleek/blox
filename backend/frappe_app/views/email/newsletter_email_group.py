from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.newsletter_email_group import NewsletterEmailGroup
from frappe_app.filters.email.newsletter_email_group import NewsletterEmailGroupFilter
from frappe_app.serializers.email.newsletter_email_group import NewsletterEmailGroupSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NewsletterEmailGroupViewSet(GenericViewSet):
    queryset = NewsletterEmailGroup.objects.all()
    filterset_class = NewsletterEmailGroupFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NewsletterEmailGroupSerializer

