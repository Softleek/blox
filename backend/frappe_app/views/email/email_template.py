from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_template import EmailTemplate
from frappe_app.filters.email.email_template import EmailTemplateFilter
from frappe_app.serializers.email.email_template import EmailTemplateSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailTemplateViewSet(GenericViewSet):
    queryset = EmailTemplate.objects.all()
    filterset_class = EmailTemplateFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailTemplateSerializer

