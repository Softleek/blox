# Generated by Django 4.2.5 on 2025-03-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frappe_app", "0005_alter_systemsettings_reset_password_link_expiry_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autoemailreport",
            name="no_of_rows",
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name="blogsettings",
            name="comment_limit",
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name="blogsettings",
            name="like_limit",
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name="bulkupdate",
            name="limit",
            field=models.IntegerField(blank=True, default=500, null=True),
        ),
        migrations.AlterField(
            model_name="customdocperm",
            name="permlevel",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="customfield",
            name="permlevel",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="customizeformfield",
            name="permlevel",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="docfield",
            name="permlevel",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="docperm",
            name="permlevel",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="doctype",
            name="grid_page_length",
            field=models.IntegerField(blank=True, default=50, null=True),
        ),
        migrations.AlterField(
            model_name="documentnamingrule",
            name="counter",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="documentnamingrule",
            name="prefix_digits",
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name="dropboxsettings",
            name="no_of_backups",
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name="emailaccount",
            name="unreplied_for_mins",
            field=models.IntegerField(blank=True, default=30, null=True),
        ),
        migrations.AlterField(
            model_name="emailgroup",
            name="total_subscribers",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="emailqueue",
            name="priority",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name="emailqueue",
            name="retry",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="formtourstep",
            name="offset_x",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="formtourstep",
            name="offset_y",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="helparticle",
            name="helpful",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="helparticle",
            name="not_helpful",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="logstoclear",
            name="days",
            field=models.IntegerField(blank=True, default=30, null=True),
        ),
        migrations.AlterField(
            model_name="networkprintersettings",
            name="port",
            field=models.IntegerField(blank=True, default=631, null=True),
        ),
        migrations.AlterField(
            model_name="newsletter",
            name="total_views",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="notification",
            name="days_in_advance",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="notification",
            name="minutes_offset",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="printformat",
            name="font_size",
            field=models.IntegerField(blank=True, default=14, null=True),
        ),
        migrations.AlterField(
            model_name="printformat",
            name="margin_bottom",
            field=models.FloatField(blank=True, default=15.0, null=True),
        ),
        migrations.AlterField(
            model_name="printformat",
            name="margin_left",
            field=models.FloatField(blank=True, default=15.0, null=True),
        ),
        migrations.AlterField(
            model_name="printformat",
            name="margin_right",
            field=models.FloatField(blank=True, default=15.0, null=True),
        ),
        migrations.AlterField(
            model_name="printformat",
            name="margin_top",
            field=models.FloatField(blank=True, default=15.0, null=True),
        ),
        migrations.AlterField(
            model_name="serverscript",
            name="rate_limit_count",
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name="serverscript",
            name="rate_limit_seconds",
            field=models.IntegerField(blank=True, default=86400, null=True),
        ),
        migrations.AlterField(
            model_name="successaction",
            name="action_timeout",
            field=models.IntegerField(blank=True, default=7, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="allow_consecutive_login_attempts",
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="allow_error_traceback",
            field=models.BooleanField(blank=True, default="1", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="allow_guests_to_upload_files",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="allow_login_after_fail",
            field=models.IntegerField(blank=True, default=60, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="allow_login_using_mobile_number",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="allow_login_using_user_name",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="allow_older_web_view_links",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="apply_strict_user_permissions",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="attach_view_link",
            field=models.BooleanField(blank=True, default="1", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="backup_limit",
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="bypass_2fa_for_retricted_ip_users",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="bypass_restrict_ip_check_if_2fa_enabled",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="deny_multiple_sessions",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="disable_change_log_notification",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="disable_document_sharing",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="disable_standard_email_footer",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="disable_system_update_notification",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="disable_user_pass_login",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="document_share_key_expiry",
            field=models.IntegerField(blank=True, default=30, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="dormant_days",
            field=models.IntegerField(blank=True, default=4, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="email_retry_limit",
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="enable_onboarding",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="enable_password_policy",
            field=models.BooleanField(blank=True, default="1", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="enable_scheduler",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="enable_telemetry",
            field=models.BooleanField(blank=True, default="1", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="enable_two_factor_auth",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="encrypt_backup",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="force_web_capture_mode_for_uploads",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="hide_empty_read_only_fields",
            field=models.BooleanField(blank=True, default="1", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="hide_footer_in_auto_email_reports",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="link_field_results_limit",
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="login_with_email_link",
            field=models.BooleanField(blank=True, default="1", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="login_with_email_link_expiry",
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="logout_on_password_reset",
            field=models.BooleanField(blank=True, default="1", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="max_auto_email_report_per_user",
            field=models.IntegerField(blank=True, default=20, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="password_reset_limit",
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="reset_password_link_expiry_duration",
            field=models.DurationField(blank=True, default='"0:20:00"', null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="setup_complete",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="store_attached_pdf_document",
            field=models.BooleanField(blank=True, default="1", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="strip_exif_metadata_from_uploaded_images",
            field=models.BooleanField(blank=True, default="1", null=True),
        ),
        migrations.AlterField(
            model_name="systemsettings",
            name="use_number_format_from_currency",
            field=models.BooleanField(blank=True, default="0", null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="simultaneous_sessions",
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
        migrations.AlterField(
            model_name="webhook",
            name="timeout",
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name="websitesettings",
            name="auto_account_deletion",
            field=models.IntegerField(blank=True, default=72, null=True),
        ),
    ]
