from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.todo import ToDo

class ToDoSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'
