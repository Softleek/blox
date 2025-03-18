from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class User(BaseModel):
    enabled = models.BooleanField(default=True, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    send_welcome_email = models.BooleanField(default=True, null=True, blank=True)
    unsubscribed = models.BooleanField(default=False, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    language = models.ForeignKey("frappe_app.Language", related_name="UserLanguage", on_delete=models.CASCADE, null=True, blank=True)
    time_zone = models.CharField(max_length=255, null=True, blank=True)
    user_image = models.CharField(max_length=255, null=True, blank=True)
    role_profile_name = models.ForeignKey("frappe_app.RoleProfile", related_name="UserRoleProfileName", on_delete=models.CASCADE, null=True, blank=True)
    roles_html = models.TextField(null=True, blank=True)
    roles = models.ManyToManyField("frappe_app.HasRole", related_name="UserRoles", )
    gender = models.ForeignKey("frappe_app.Gender", related_name="UserGender", on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    mobile_no = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    banner_image = models.CharField(max_length=255, null=True, blank=True)
    interest = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    mute_sounds = models.BooleanField(default=False, null=True, blank=True)
    new_password = models.CharField(max_length=255, null=True, blank=True)
    logout_all_sessions = models.BooleanField(default=True, null=True, blank=True)
    reset_password_key = models.CharField(max_length=255, null=True, blank=True)
    last_password_reset_date = models.DateField(null=True, blank=True)
    redirect_url = models.TextField(null=True, blank=True)
    document_follow_notify = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_DOCUMENT_FOLLOW_FREQUENCY = [
        ("Hourly", "Hourly"),
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
    ]
    document_follow_frequency = models.CharField(choices=CHOICES_DOCUMENT_FOLLOW_FREQUENCY, max_length=255, default='Daily', null=True, blank=True)
    thread_notify = models.BooleanField(default=True, null=True, blank=True)
    send_me_a_copy = models.BooleanField(default=False, null=True, blank=True)
    allowed_in_mentions = models.BooleanField(default=True, null=True, blank=True)
    email_signature = models.CharField(max_length=255, null=True, blank=True)
    user_emails = models.ManyToManyField("frappe_app.UserEmail", related_name="UserUserEmails", )
    modules_html = models.TextField(null=True, blank=True)
    block_modules = models.ManyToManyField("frappe_app.BlockModule", related_name="UserBlockModules", )
    home_settings = models.CharField(max_length=255, null=True, blank=True)
    defaults = models.ManyToManyField("frappe_app.Defaultvalue", related_name="UserDefaults", )
    simultaneous_sessions = models.IntegerField(default=2, null=True, blank=True)
    user_type = models.ForeignKey("frappe_app.UserType", related_name="UserUserType", on_delete=models.CASCADE, default='System User', null=True, blank=True)
    login_after = models.IntegerField(null=True, blank=True)
    login_before = models.IntegerField(null=True, blank=True)
    restrict_ip = models.TextField(null=True, blank=True)
    bypass_restrict_ip_check_if_2fa_enabled = models.BooleanField(default=False, null=True, blank=True)
    last_login = models.CharField(max_length=255, null=True, blank=True)
    last_ip = models.CharField(max_length=255, null=True, blank=True)
    last_active = models.DateTimeField(null=True, blank=True)
    last_known_versions = models.TextField(null=True, blank=True)
    social_logins = models.ManyToManyField("frappe_app.UserSocialLogin", related_name="UserSocialLogins", )
    api_key = models.CharField(max_length=255, null=True, blank=True)
    generate_keys = models.CharField(max_length=255, null=True, blank=True)
    api_secret = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_DESK_THEME = [
        ("Light", "Light"),
        ("Dark", "Dark"),
        ("Automatic", "Automatic"),
    ]
    desk_theme = models.CharField(choices=CHOICES_DESK_THEME, max_length=255, null=True, blank=True)
    module_profile = models.ForeignKey("frappe_app.ModuleProfile", related_name="UserModuleProfile", on_delete=models.CASCADE, null=True, blank=True)
    last_reset_password_key_generated_on = models.DateTimeField(null=True, blank=True)
    follow_created_documents = models.BooleanField(default=False, null=True, blank=True)
    follow_commented_documents = models.BooleanField(default=False, null=True, blank=True)
    follow_liked_documents = models.BooleanField(default=False, null=True, blank=True)
    follow_shared_documents = models.BooleanField(default=False, null=True, blank=True)
    follow_assigned_documents = models.BooleanField(default=False, null=True, blank=True)
    onboarding_status = models.TextField(default='{}', null=True, blank=True)
    role_profiles = models.ManyToManyField("frappe_app.UserRoleProfile", related_name="UserRoleProfiles", )
    default_workspace = models.ForeignKey("frappe_app.Workspace", related_name="UserDefaultWorkspace", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_CODE_EDITOR_TYPE = [
        ("vscode", "vscode"),
        ("vim", "vim"),
        ("emacs", "emacs"),
    ]
    code_editor_type = models.CharField(choices=CHOICES_CODE_EDITOR_TYPE, max_length=255, default='vscode', null=True, blank=True)
    CHOICES_DEFAULT_APP = [
        ("", ""),
    ]
    default_app = models.CharField(choices=CHOICES_DEFAULT_APP, max_length=255, null=True, blank=True)
    search_bar = models.BooleanField(default=True, null=True, blank=True)
    notifications = models.BooleanField(default=True, null=True, blank=True)
    list_sidebar = models.BooleanField(default=True, null=True, blank=True)
    bulk_actions = models.BooleanField(default=True, null=True, blank=True)
    view_switcher = models.BooleanField(default=True, null=True, blank=True)
    form_sidebar = models.BooleanField(default=True, null=True, blank=True)
    timeline = models.BooleanField(default=True, null=True, blank=True)
    dashboard = models.BooleanField(default=True, null=True, blank=True)
