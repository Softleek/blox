from core.models import App, ChangeLog, Document, Module, User, Reminder
from django.contrib.auth.models import Group
from django_filters import rest_framework as filters

from .template import DynamicFilterSet

from core.models.auth import RoleType, Branch

class AppFilter(DynamicFilterSet):
    class Meta:
        model = App
        fields = "__all__"
        exclude = ["app_icon"]


class ModuleFilter(DynamicFilterSet):
    class Meta:
        model = Module
        fields = "__all__"
        exclude = ["edit_history"]


class DocumentFilter(DynamicFilterSet):
    class Meta:
        model = Document
        fields = "__all__"
        exclude = ["edit_history"]


class ChangeLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')
    model_name = filters.CharFilter(lookup_expr='icontains', label='Model Name')
    object_id = filters.CharFilter(lookup_expr='icontains', label='Obejct ID')

    class Meta:
        model = ChangeLog
        fields = ["id", "model_name", "object_id"]
        


class UserFilter(DynamicFilterSet):
    class Meta:
        model = User
        fields = "__all__"
        exclude = ["profile_picture"]


class ReminderFilter(filters.FilterSet):
    class Meta:
        model = Reminder
        fields = ['id', 'date', 'time', 'message', 'next_run', 'created', 'modified']

class GroupFilter(filters.FilterSet):
    class Meta:
        model = Group
        fields = "__all__"
        
        
class PermissionFilter(filters.FilterSet):
    class Meta:
        model = Group
        fields = "__all__"     
        
           
class RoleFilter(filters.FilterSet):
    class Meta:
        model = RoleType
        fields = "__all__"
class BranchFilter(filters.FilterSet):
    class Meta:
        model = Branch
        fields = "__all__"