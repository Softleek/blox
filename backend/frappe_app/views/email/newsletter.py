from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.newsletter import Newsletter
from frappe_app.filters.email.newsletter import NewsletterFilter
from frappe_app.serializers.email.newsletter import NewsletterSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NewsletterViewSet(GenericViewSet):
    queryset = Newsletter.objects.all()
    filterset_class = NewsletterFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NewsletterSerializer

