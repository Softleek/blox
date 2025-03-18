from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SystemSettings(SingletonModel):
    country = models.ForeignKey("frappe_app.Country", related_name="SystemSettingsCountry", on_delete=models.CASCADE, null=True, blank=True)
    language = models.ForeignKey("frappe_app.Language", related_name="SystemSettingsLanguage", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_TIME_ZONE = [
        ("", ""),
    ]
    time_zone = models.CharField(choices=CHOICES_TIME_ZONE, max_length=255, null=True, blank=True)
    setup_complete = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_DATE_FORMAT = [
        ("yyyy-mm-dd", "yyyy-mm-dd"),
        ("dd-mm-yyyy", "dd-mm-yyyy"),
        ("dd/mm/yyyy", "dd/mm/yyyy"),
        ("dd.mm.yyyy", "dd.mm.yyyy"),
        ("mm/dd/yyyy", "mm/dd/yyyy"),
        ("mm-dd-yyyy", "mm-dd-yyyy"),
    ]
    date_format = models.CharField(choices=CHOICES_DATE_FORMAT, max_length=255, null=True, blank=True)
    CHOICES_TIME_FORMAT = [
        ("HH:mm:ss", "HH:mm:ss"),
        ("HH:mm", "HH:mm"),
    ]
    time_format = models.CharField(choices=CHOICES_TIME_FORMAT, max_length=255, default='HH:mm:ss', null=True, blank=True)
    CHOICES_NUMBER_FORMAT = [
        ("#,###.##", "#,###.##"),
        ("#.###,##", "#.###,##"),
        ("# ###.##", "# ###.##"),
        ("# ###,##", "# ###,##"),
        ("#'###.##", "#'###.##"),
        ("#, ###.##", "#, ###.##"),
        ("#,##,###.##", "#,##,###.##"),
        ("#,###.###", "#,###.###"),
        ("#.###", "#.###"),
        ("#,###", "#,###"),
    ]
    number_format = models.CharField(choices=CHOICES_NUMBER_FORMAT, max_length=255, null=True, blank=True)
    CHOICES_FLOAT_PRECISION = [
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    ]
    float_precision = models.CharField(choices=CHOICES_FLOAT_PRECISION, max_length=255, null=True, blank=True)
    CHOICES_CURRENCY_PRECISION = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    ]
    currency_precision = models.CharField(choices=CHOICES_CURRENCY_PRECISION, max_length=255, null=True, blank=True)
    backup_limit = models.IntegerField(default=3, null=True, blank=True)
    enable_scheduler = models.BooleanField(default=False, null=True, blank=True)
    apply_strict_user_permissions = models.BooleanField(default=False, null=True, blank=True)
    session_expiry = models.CharField(max_length=255, default='170:00', null=True, blank=True)
    deny_multiple_sessions = models.BooleanField(default=False, null=True, blank=True)
    allow_login_using_mobile_number = models.BooleanField(default=False, null=True, blank=True)
    allow_login_using_user_name = models.BooleanField(default=False, null=True, blank=True)
    allow_error_traceback = models.BooleanField(default=True, null=True, blank=True)
    force_user_to_reset_password = models.IntegerField(null=True, blank=True)
    enable_password_policy = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_MINIMUM_PASSWORD_SCORE = [
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    ]
    minimum_password_score = models.CharField(choices=CHOICES_MINIMUM_PASSWORD_SCORE, max_length=255, default='2', null=True, blank=True)
    allow_consecutive_login_attempts = models.IntegerField(default=10, null=True, blank=True)
    allow_login_after_fail = models.IntegerField(default=60, null=True, blank=True)
    enable_two_factor_auth = models.BooleanField(default=False, null=True, blank=True)
    bypass_2fa_for_retricted_ip_users = models.BooleanField(default=False, null=True, blank=True)
    bypass_restrict_ip_check_if_2fa_enabled = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_TWO_FACTOR_METHOD = [
        ("OTP App", "OTP App"),
        ("SMS", "SMS"),
        ("Email", "Email"),
    ]
    two_factor_method = models.CharField(choices=CHOICES_TWO_FACTOR_METHOD, max_length=255, default='OTP App', null=True, blank=True)
    lifespan_qrcode_image = models.IntegerField(null=True, blank=True)
    otp_issuer_name = models.CharField(max_length=255, default='Frappe Framework', null=True, blank=True)
    email_footer_address = models.TextField(null=True, blank=True)
    disable_standard_email_footer = models.BooleanField(default=False, null=True, blank=True)
    hide_footer_in_auto_email_reports = models.BooleanField(default=False, null=True, blank=True)
    allow_guests_to_upload_files = models.BooleanField(default=False, null=True, blank=True)
    dormant_days = models.IntegerField(default=4, null=True, blank=True)
    password_reset_limit = models.IntegerField(default=3, null=True, blank=True)
    logout_on_password_reset = models.BooleanField(default=True, null=True, blank=True)
    enable_onboarding = models.BooleanField(default=False, null=True, blank=True)
    attach_view_link = models.BooleanField(default=True, null=True, blank=True)
    app_name = models.CharField(max_length=255, default='Frappe', null=True, blank=True)
    strip_exif_metadata_from_uploaded_images = models.BooleanField(default=True, null=True, blank=True)
    encrypt_backup = models.BooleanField(default=False, null=True, blank=True)
    disable_system_update_notification = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_FIRST_DAY_OF_THE_WEEK = [
        ("Sunday", "Sunday"),
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
    ]
    first_day_of_the_week = models.CharField(choices=CHOICES_FIRST_DAY_OF_THE_WEEK, max_length=255, default='Sunday', null=True, blank=True)
    document_share_key_expiry = models.IntegerField(default=30, null=True, blank=True)
    allow_older_web_view_links = models.BooleanField(default=False, null=True, blank=True)
    max_auto_email_report_per_user = models.IntegerField(default=20, null=True, blank=True)
    disable_change_log_notification = models.BooleanField(default=False, null=True, blank=True)
    reset_password_link_expiry_duration = models.DurationField(default='"0:20:00"', null=True, blank=True)
    email_retry_limit = models.IntegerField(default=3, null=True, blank=True)
    disable_user_pass_login = models.BooleanField(default=False, null=True, blank=True)
    login_with_email_link = models.BooleanField(default=True, null=True, blank=True)
    login_with_email_link_expiry = models.IntegerField(default=10, null=True, blank=True)
    CHOICES_ROUNDING_METHOD = [
        ("Banker's Rounding (legacy)", "Banker's Rounding (legacy)"),
        ("Banker's Rounding", "Banker's Rounding"),
        ("Commercial Rounding", "Commercial Rounding"),
    ]
    rounding_method = models.CharField(choices=CHOICES_ROUNDING_METHOD, max_length=255, default="Banker's Rounding (legacy)", null=True, blank=True)
    disable_document_sharing = models.BooleanField(default=False, null=True, blank=True)
    enable_telemetry = models.BooleanField(default=True, null=True, blank=True)
    welcome_email_template = models.ForeignKey("frappe_app.EmailTemplate", related_name="SystemSettingsWelcomeEmailTemplate", on_delete=models.CASCADE, null=True, blank=True)
    reset_password_template = models.ForeignKey("frappe_app.EmailTemplate", related_name="SystemSettingsResetPasswordTemplate", on_delete=models.CASCADE, null=True, blank=True)
    force_web_capture_mode_for_uploads = models.BooleanField(default=False, null=True, blank=True)
    max_file_size = models.IntegerField(null=True, blank=True)
    allowed_file_extensions = models.TextField(null=True, blank=True)
    link_field_results_limit = models.IntegerField(default=10, null=True, blank=True)
    store_attached_pdf_document = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_DEFAULT_APP = [
        ("", ""),
    ]
    default_app = models.CharField(choices=CHOICES_DEFAULT_APP, max_length=255, null=True, blank=True)
    rate_limit_email_link_login = models.IntegerField(null=True, blank=True)
    use_number_format_from_currency = models.BooleanField(default=False, null=True, blank=True)
    currency = models.ForeignKey("frappe_app.Currency", related_name="SystemSettingsCurrency", on_delete=models.CASCADE, null=True, blank=True)
    hide_empty_read_only_fields = models.BooleanField(default=True, null=True, blank=True)
