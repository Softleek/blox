from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.newsletter_attachment import NewsletterAttachment
from frappe_app.filters.email.newsletter_attachment import NewsletterAttachmentFilter
from frappe_app.serializers.email.newsletter_attachment import NewsletterAttachmentSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NewsletterAttachmentViewSet(GenericViewSet):
    queryset = NewsletterAttachment.objects.all()
    filterset_class = NewsletterAttachmentFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NewsletterAttachmentSerializer

