from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.todo import ToDo
from frappe_app.filters.desk.todo import ToDoFilter
from frappe_app.serializers.desk.todo import ToDoSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ToDoViewSet(GenericViewSet):
    queryset = ToDo.objects.all()
    filterset_class = ToDoFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ToDoSerializer

