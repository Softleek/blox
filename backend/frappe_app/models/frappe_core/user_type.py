from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class UserType(BaseModel):
    is_standard = models.BooleanField(default=False, null=True, blank=True)
    user_doctypes = models.ManyToManyField("frappe_app.UserDocumentType", related_name="UserTypeUserDoctypes", )
    role = models.ForeignKey("frappe_app.Role", related_name="UserTypeRole", on_delete=models.CASCADE, null=True, blank=True)
    select_doctypes = models.ManyToManyField("frappe_app.UserSelectDocumentType", related_name="UserTypeSelectDoctypes", )
    apply_user_permission_on = models.ForeignKey("frappe_app.Doctype", related_name="UserTypeApplyUserPermissionOn", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_USER_ID_FIELD = [
        ("", ""),
    ]
    user_id_field = models.CharField(choices=CHOICES_USER_ID_FIELD, max_length=255, null=True, blank=True)
    user_type_modules = models.ManyToManyField("frappe_app.UserTypeModule", related_name="UserTypeUserTypeModules", )
    custom_select_doctypes = models.ManyToManyField("frappe_app.UserSelectDocumentType", related_name="UserTypeCustomSelectDoctypes", )
