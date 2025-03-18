

from frappe.core.doctype.permission_inspector.permission_inspector import *
from frappe.core.doctype.page.page import *
from frappe.core.doctype.user.user import *
from frappe.core.doctype.amended_document_naming_settings.amended_document_naming_settings import *
from frappe.core.doctype.docperm.docperm import *
from frappe.core.doctype.custom_role.custom_role import *
from frappe.core.doctype.sms_log.sms_log import *
from frappe.core.doctype.error_log.error_log import *
from frappe.core.doctype.block_module.block_module import *
from frappe.core.doctype.navbar_settings.navbar_settings import *
from frappe.core.doctype.custom_docperm.custom_docperm import *
from frappe.core.doctype.doctype_state.doctype_state import *
from frappe.core.doctype.access_log.access_log import *
from frappe.core.doctype.data_import_log.data_import_log import *
from frappe.core.doctype.document_naming_rule.document_naming_rule import *
from frappe.core.doctype.communication_link.communication_link import *
from frappe.core.doctype.view_log.view_log import *
from frappe.core.doctype.prepared_report.prepared_report import *
from frappe.core.doctype.has_role.has_role import *
from frappe.core.doctype.role_profile.role_profile import *
from frappe.core.doctype.rq_job.rq_job import *
from frappe.core.doctype.user_select_document_type.user_select_document_type import *
from frappe.core.doctype.file.file import *
from frappe.core.doctype.log_setting_user.log_setting_user import *
from frappe.core.doctype.recorder_suggested_index.recorder_suggested_index import *
from frappe.core.doctype.domain.domain import *
from frappe.core.doctype.document_share_key.document_share_key import *
from frappe.core.doctype.log_settings.log_settings import *
from frappe.core.doctype.user_group.user_group import *
from frappe.core.doctype.package_import.package_import import *
from frappe.core.doctype.language.language import *
from frappe.core.doctype.comment.comment import *
from frappe.core.doctype.navbar_item.navbar_item import *
from frappe.core.doctype.user_permission.user_permission import *
from frappe.core.doctype.user_type.user_type import *
from frappe.core.doctype.docfield.docfield import *
from frappe.core.doctype.user_group_member.user_group_member import *
from frappe.core.doctype.system_settings.system_settings import *
from frappe.core.doctype.installed_application.installed_application import *
from frappe.core.doctype.role_permission_for_page_and_report.role_permission_for_page_and_report import *
from frappe.core.doctype.package_release.package_release import *
from frappe.core.doctype.doctype_link.doctype_link import *
from frappe.core.doctype.submission_queue.submission_queue import *
from frappe.core.doctype.data_import.data_import import *
from frappe.core.doctype.sms_settings.sms_settings import *
from frappe.core.doctype.user_document_type.user_document_type import *
from frappe.core.doctype.user_email.user_email import *
from frappe.core.doctype.version.version import *
from frappe.core.doctype.dynamic_link.dynamic_link import *
from frappe.core.doctype.recorder_query.recorder_query import *
from frappe.core.doctype.transaction_log.transaction_log import *
from frappe.core.doctype.role.role import *
from frappe.core.doctype.installed_applications.installed_applications import *
from frappe.core.doctype.translation.translation import *
from frappe.core.doctype.document_naming_rule_condition.document_naming_rule_condition import *
from frappe.core.doctype.role_replication.role_replication import *
from frappe.core.doctype.user_type_module.user_type_module import *
from frappe.core.doctype.server_script.server_script import *
from frappe.core.doctype.session_default.session_default import *
from frappe.core.doctype.docshare.docshare import *
from frappe.core.doctype.data_export.data_export import *
from frappe.core.doctype.sms_parameter.sms_parameter import *
from frappe.core.doctype.user_social_login.user_social_login import *
from frappe.core.doctype.defaultvalue.defaultvalue import *
from frappe.core.doctype.report_column.report_column import *
from frappe.core.doctype.module_def.module_def import *
from frappe.core.doctype.package.package import *
from frappe.core.doctype.session_default_settings.session_default_settings import *
from frappe.core.doctype.document_naming_settings.document_naming_settings import *
from frappe.core.doctype.doctype.doctype import *
from frappe.core.doctype.user_role_profile.user_role_profile import *
from frappe.core.doctype.report_filter.report_filter import *
from frappe.core.doctype.domain_settings.domain_settings import *
from frappe.core.doctype.success_action.success_action import *
from frappe.core.doctype.recorder.recorder import *
from frappe.core.doctype.activity_log.activity_log import *
from frappe.core.doctype.module_profile.module_profile import *
from frappe.core.doctype.doctype_action.doctype_action import *
from frappe.core.doctype.rq_worker.rq_worker import *
from frappe.core.doctype.scheduled_job_type.scheduled_job_type import *
from frappe.core.doctype.audit_trail.audit_trail import *
from frappe.core.doctype.permission_log.permission_log import *
from frappe.core.doctype.deleted_document.deleted_document import *
from frappe.core.doctype.communication.communication import *
from frappe.core.doctype.scheduled_job_log.scheduled_job_log import *
from frappe.core.doctype.scheduler_event.scheduler_event import *
from frappe.core.doctype.has_domain.has_domain import *
from frappe.core.doctype.report.report import *
from frappe.core.doctype.logs_to_clear.logs_to_clear import *
from frappe.core.doctype.patch_log.patch_log import *
from frappe.website.doctype.utm_source.utm_source import *
from frappe.website.doctype.color.color import *
from frappe.website.doctype.web_form.web_form import *
from frappe.website.doctype.help_category.help_category import *
from frappe.website.doctype.utm_campaign.utm_campaign import *
from frappe.website.doctype.company_history.company_history import *
from frappe.website.doctype.social_link_settings.social_link_settings import *
from frappe.website.doctype.web_page_view.web_page_view import *
from frappe.website.doctype.contact_us_settings.contact_us_settings import *
from frappe.website.doctype.website_slideshow_item.website_slideshow_item import *
from frappe.website.doctype.about_us_settings.about_us_settings import *
from frappe.website.doctype.website_script.website_script import *
from frappe.website.doctype.utm_medium.utm_medium import *
from frappe.website.doctype.website_sidebar_item.website_sidebar_item import *
from frappe.website.doctype.web_template.web_template import *
from frappe.website.doctype.blog_settings.blog_settings import *
from frappe.website.doctype.website_meta_tag.website_meta_tag import *
from frappe.website.doctype.website_theme_ignore_app.website_theme_ignore_app import *
from frappe.website.doctype.web_page.web_page import *
from frappe.website.doctype.portal_menu_item.portal_menu_item import *
from frappe.website.doctype.website_route_redirect.website_route_redirect import *
from frappe.website.doctype.help_article.help_article import *
from frappe.website.doctype.web_page_block.web_page_block import *
from frappe.website.doctype.portal_settings.portal_settings import *
from frappe.website.doctype.web_template_field.web_template_field import *
from frappe.website.doctype.about_us_team_member.about_us_team_member import *
from frappe.website.doctype.website_route_meta.website_route_meta import *
from frappe.website.doctype.blogger.blogger import *
from frappe.website.doctype.personal_data_deletion_request.personal_data_deletion_request import *
from frappe.website.doctype.discussion_reply.discussion_reply import *
from frappe.website.doctype.web_form_field.web_form_field import *
from frappe.website.doctype.personal_data_deletion_step.personal_data_deletion_step import *
from frappe.website.doctype.website_settings.website_settings import *
from frappe.website.doctype.website_sidebar.website_sidebar import *
from frappe.website.doctype.website_slideshow.website_slideshow import *
from frappe.website.doctype.personal_data_download_request.personal_data_download_request import *
from frappe.website.doctype.top_bar_item.top_bar_item import *
from frappe.website.doctype.blog_post.blog_post import *
from frappe.website.doctype.discussion_topic.discussion_topic import *
from frappe.website.doctype.blog_category.blog_category import *
from frappe.website.doctype.website_theme.website_theme import *
from frappe.website.doctype.web_form_list_column.web_form_list_column import *
from frappe.workflow.doctype.workflow_state.workflow_state import *
from frappe.workflow.doctype.workflow_document_state.workflow_document_state import *
from frappe.workflow.doctype.workflow_action_master.workflow_action_master import *
from frappe.workflow.doctype.workflow.workflow import *
from frappe.workflow.doctype.workflow_transition.workflow_transition import *
from frappe.workflow.doctype.workflow_action.workflow_action import *
from frappe.workflow.doctype.workflow_action_permitted_role.workflow_action_permitted_role import *
from frappe.email.doctype.email_account.email_account import *
from frappe.email.doctype.document_follow.document_follow import *
from frappe.email.doctype.unhandled_email.unhandled_email import *
from frappe.email.doctype.email_unsubscribe.email_unsubscribe import *
from frappe.email.doctype.email_flag_queue.email_flag_queue import *
from frappe.email.doctype.notification_recipient.notification_recipient import *
from frappe.email.doctype.auto_email_report.auto_email_report import *
from frappe.email.doctype.newsletter_email_group.newsletter_email_group import *
from frappe.email.doctype.email_group_member.email_group_member import *
from frappe.email.doctype.email_queue_recipient.email_queue_recipient import *
from frappe.email.doctype.notification.notification import *
from frappe.email.doctype.email_queue.email_queue import *
from frappe.email.doctype.email_group.email_group import *
from frappe.email.doctype.newsletter.newsletter import *
from frappe.email.doctype.email_rule.email_rule import *
from frappe.email.doctype.newsletter_attachment.newsletter_attachment import *
from frappe.email.doctype.email_domain.email_domain import *
from frappe.email.doctype.imap_folder.imap_folder import *
from frappe.email.doctype.email_template.email_template import *
from frappe.custom.doctype.custom_field.custom_field import *
from frappe.custom.doctype.customize_form.customize_form import *
from frappe.custom.doctype.doctype_layout_field.doctype_layout_field import *
from frappe.custom.doctype.customize_form_field.customize_form_field import *
from frappe.custom.doctype.doctype_layout.doctype_layout import *
from frappe.custom.doctype.client_script.client_script import *
from frappe.custom.doctype.property_setter.property_setter import *
from frappe.geo.doctype.country.country import *
from frappe.geo.doctype.currency.currency import *
from frappe.desk.doctype.dashboard_chart_link.dashboard_chart_link import *
from frappe.desk.doctype.route_history.route_history import *
from frappe.desk.doctype.notification_log.notification_log import *
from frappe.desk.doctype.form_tour.form_tour import *
from frappe.desk.doctype.dashboard_chart_field.dashboard_chart_field import *
from frappe.desk.doctype.console_log.console_log import *
from frappe.desk.doctype.onboarding_permission.onboarding_permission import *
from frappe.desk.doctype.workspace_quick_list.workspace_quick_list import *
from frappe.desk.doctype.notification_settings.notification_settings import *
from frappe.desk.doctype.workspace_shortcut.workspace_shortcut import *
from frappe.desk.doctype.calendar_view.calendar_view import *
from frappe.desk.doctype.number_card_link.number_card_link import *
from frappe.desk.doctype.bulk_update.bulk_update import *
from frappe.desk.doctype.workspace_settings.workspace_settings import *
from frappe.desk.doctype.note_seen_by.note_seen_by import *
from frappe.desk.doctype.workspace_custom_block.workspace_custom_block import *
from frappe.desk.doctype.system_console.system_console import *
from frappe.desk.doctype.tag_link.tag_link import *
from frappe.desk.doctype.todo.todo import *
from frappe.desk.doctype.dashboard_chart.dashboard_chart import *
from frappe.desk.doctype.dashboard_chart_source.dashboard_chart_source import *
from frappe.desk.doctype.system_health_report_errors.system_health_report_errors import *
from frappe.desk.doctype.tag.tag import *
from frappe.desk.doctype.list_filter.list_filter import *
from frappe.desk.doctype.event_participants.event_participants import *
from frappe.desk.doctype.list_view_settings.list_view_settings import *
from frappe.desk.doctype.global_search_doctype.global_search_doctype import *
from frappe.desk.doctype.notification_subscribed_document.notification_subscribed_document import *
from frappe.desk.doctype.number_card.number_card import *
from frappe.desk.doctype.system_health_report_queue.system_health_report_queue import *
from frappe.desk.doctype.dashboard.dashboard import *
from frappe.desk.doctype.onboarding_step_map.onboarding_step_map import *
from frappe.desk.doctype.system_health_report.system_health_report import *
from frappe.desk.doctype.kanban_board_column.kanban_board_column import *
from frappe.desk.doctype.global_search_settings.global_search_settings import *
from frappe.desk.doctype.system_health_report_tables.system_health_report_tables import *
from frappe.desk.doctype.kanban_board.kanban_board import *
from frappe.desk.doctype.desktop_icon.desktop_icon import *
from frappe.desk.doctype.system_health_report_failing_jobs.system_health_report_failing_jobs import *
from frappe.desk.doctype.workspace_number_card.workspace_number_card import *
from frappe.desk.doctype.event.event import *
from frappe.desk.doctype.form_tour_step.form_tour_step import *
from frappe.desk.doctype.onboarding_step.onboarding_step import *
from frappe.desk.doctype.module_onboarding.module_onboarding import *
from frappe.desk.doctype.dashboard_settings.dashboard_settings import *
from frappe.desk.doctype.changelog_feed.changelog_feed import *
from frappe.desk.doctype.workspace_chart.workspace_chart import *
from frappe.desk.doctype.note.note import *
from frappe.desk.doctype.workspace.workspace import *
from frappe.desk.doctype.system_health_report_workers.system_health_report_workers import *
from frappe.desk.doctype.workspace_link.workspace_link import *
from frappe.desk.doctype.custom_html_block.custom_html_block import *
from frappe.integrations.doctype.google_contacts.google_contacts import *
from frappe.integrations.doctype.oauth_client.oauth_client import *
from frappe.integrations.doctype.oauth_authorization_code.oauth_authorization_code import *
from frappe.integrations.doctype.integration_request.integration_request import *
from frappe.integrations.doctype.oauth_bearer_token.oauth_bearer_token import *
from frappe.integrations.doctype.token_cache.token_cache import *
from frappe.integrations.doctype.google_calendar.google_calendar import *
from frappe.integrations.doctype.slack_webhook_url.slack_webhook_url import *
from frappe.integrations.doctype.oauth_client_role.oauth_client_role import *
from frappe.integrations.doctype.push_notification_settings.push_notification_settings import *
from frappe.integrations.doctype.social_login_key.social_login_key import *
from frappe.integrations.doctype.webhook_request_log.webhook_request_log import *
from frappe.integrations.doctype.ldap_settings.ldap_settings import *
from frappe.integrations.doctype.connected_app.connected_app import *
from frappe.integrations.doctype.oauth_scope.oauth_scope import *
from frappe.integrations.doctype.dropbox_settings.dropbox_settings import *
from frappe.integrations.doctype.social_login_keys.social_login_keys import *
from frappe.integrations.doctype.google_drive.google_drive import *
from frappe.integrations.doctype.oauth_provider_settings.oauth_provider_settings import *
from frappe.integrations.doctype.google_settings.google_settings import *
from frappe.integrations.doctype.webhook.webhook import *
from frappe.integrations.doctype.webhook_data.webhook_data import *
from frappe.integrations.doctype.query_parameters.query_parameters import *
from frappe.integrations.doctype.geolocation_settings.geolocation_settings import *
from frappe.integrations.doctype.ldap_group_mapping.ldap_group_mapping import *
from frappe.integrations.doctype.webhook_header.webhook_header import *
from frappe.integrations.doctype.s3_backup_settings.s3_backup_settings import *
from frappe.printing.doctype.letter_head.letter_head import *
from frappe.printing.doctype.print_format_field_template.print_format_field_template import *
from frappe.printing.doctype.print_settings.print_settings import *
from frappe.printing.doctype.print_heading.print_heading import *
from frappe.printing.doctype.print_format.print_format import *
from frappe.printing.doctype.print_style.print_style import *
from frappe.printing.doctype.network_printer_settings.network_printer_settings import *
from frappe.contacts.doctype.contact_email.contact_email import *
from frappe.contacts.doctype.salutation.salutation import *
from frappe.contacts.doctype.contact_phone.contact_phone import *
from frappe.contacts.doctype.contact.contact import *
from frappe.contacts.doctype.address_template.address_template import *
from frappe.contacts.doctype.gender.gender import *
from frappe.contacts.doctype.address.address import *
from frappe.social.doctype.energy_point_rule.energy_point_rule import *
from frappe.social.doctype.review_level.review_level import *
from frappe.social.doctype.energy_point_log.energy_point_log import *
from frappe.social.doctype.energy_point_settings.energy_point_settings import *
from frappe.automation.doctype.assignment_rule_day.assignment_rule_day import *
from frappe.automation.doctype.auto_repeat_day.auto_repeat_day import *
from frappe.automation.doctype.assignment_rule_user.assignment_rule_user import *
from frappe.automation.doctype.auto_repeat.auto_repeat import *
from frappe.automation.doctype.milestone.milestone import *
from frappe.automation.doctype.milestone_tracker.milestone_tracker import *
from frappe.automation.doctype.reminder.reminder import *
from frappe.automation.doctype.assignment_rule.assignment_rule import *
from frappe.frappe_core.doctype.permission_inspector.permission_inspector import *
from frappe.frappe_core.doctype.page.page import *
from frappe.frappe_core.doctype.user.user import *
from frappe.frappe_core.doctype.amended_document_naming_settings.amended_document_naming_settings import *
from frappe.frappe_core.doctype.docperm.docperm import *
from frappe.frappe_core.doctype.custom_role.custom_role import *
from frappe.frappe_core.doctype.sms_log.sms_log import *
from frappe.frappe_core.doctype.error_log.error_log import *
from frappe.frappe_core.doctype.block_module.block_module import *
from frappe.frappe_core.doctype.navbar_settings.navbar_settings import *
from frappe.frappe_core.doctype.custom_docperm.custom_docperm import *
from frappe.frappe_core.doctype.doctype_state.doctype_state import *
from frappe.frappe_core.doctype.access_log.access_log import *
from frappe.frappe_core.doctype.data_import_log.data_import_log import *
from frappe.frappe_core.doctype.document_naming_rule.document_naming_rule import *
from frappe.frappe_core.doctype.communication_link.communication_link import *
from frappe.frappe_core.doctype.view_log.view_log import *
from frappe.frappe_core.doctype.prepared_report.prepared_report import *
from frappe.frappe_core.doctype.has_role.has_role import *
from frappe.frappe_core.doctype.role_profile.role_profile import *
from frappe.frappe_core.doctype.rq_job.rq_job import *
from frappe.frappe_core.doctype.user_select_document_type.user_select_document_type import *
from frappe.frappe_core.doctype.file.file import *
from frappe.frappe_core.doctype.log_setting_user.log_setting_user import *
from frappe.frappe_core.doctype.recorder_suggested_index.recorder_suggested_index import *
from frappe.frappe_core.doctype.domain.domain import *
from frappe.frappe_core.doctype.document_share_key.document_share_key import *
from frappe.frappe_core.doctype.log_settings.log_settings import *
from frappe.frappe_core.doctype.user_group.user_group import *
from frappe.frappe_core.doctype.package_import.package_import import *
from frappe.frappe_core.doctype.language.language import *
from frappe.frappe_core.doctype.comment.comment import *
from frappe.frappe_core.doctype.navbar_item.navbar_item import *
from frappe.frappe_core.doctype.user_permission.user_permission import *
from frappe.frappe_core.doctype.user_type.user_type import *
from frappe.frappe_core.doctype.docfield.docfield import *
from frappe.frappe_core.doctype.user_group_member.user_group_member import *
from frappe.frappe_core.doctype.system_settings.system_settings import *
from frappe.frappe_core.doctype.installed_application.installed_application import *
from frappe.frappe_core.doctype.role_permission_for_page_and_report.role_permission_for_page_and_report import *
from frappe.frappe_core.doctype.package_release.package_release import *
from frappe.frappe_core.doctype.doctype_link.doctype_link import *
from frappe.frappe_core.doctype.submission_queue.submission_queue import *
from frappe.frappe_core.doctype.data_import.data_import import *
from frappe.frappe_core.doctype.sms_settings.sms_settings import *
from frappe.frappe_core.doctype.user_document_type.user_document_type import *
from frappe.frappe_core.doctype.user_email.user_email import *
from frappe.frappe_core.doctype.version.version import *
from frappe.frappe_core.doctype.dynamic_link.dynamic_link import *
from frappe.frappe_core.doctype.recorder_query.recorder_query import *
from frappe.frappe_core.doctype.transaction_log.transaction_log import *
from frappe.frappe_core.doctype.role.role import *
from frappe.frappe_core.doctype.installed_applications.installed_applications import *
from frappe.frappe_core.doctype.translation.translation import *
from frappe.frappe_core.doctype.document_naming_rule_condition.document_naming_rule_condition import *
from frappe.frappe_core.doctype.role_replication.role_replication import *
from frappe.frappe_core.doctype.user_type_module.user_type_module import *
from frappe.frappe_core.doctype.server_script.server_script import *
from frappe.frappe_core.doctype.session_default.session_default import *
from frappe.frappe_core.doctype.docshare.docshare import *
from frappe.frappe_core.doctype.data_export.data_export import *
from frappe.frappe_core.doctype.sms_parameter.sms_parameter import *
from frappe.frappe_core.doctype.user_social_login.user_social_login import *
from frappe.frappe_core.doctype.defaultvalue.defaultvalue import *
from frappe.frappe_core.doctype.report_column.report_column import *
from frappe.frappe_core.doctype.module_def.module_def import *
from frappe.frappe_core.doctype.package.package import *
from frappe.frappe_core.doctype.session_default_settings.session_default_settings import *
from frappe.frappe_core.doctype.document_naming_settings.document_naming_settings import *
from frappe.frappe_core.doctype.doctype.doctype import *
from frappe.frappe_core.doctype.user_role_profile.user_role_profile import *
from frappe.frappe_core.doctype.report_filter.report_filter import *
from frappe.frappe_core.doctype.domain_settings.domain_settings import *
from frappe.frappe_core.doctype.success_action.success_action import *
from frappe.frappe_core.doctype.recorder.recorder import *
from frappe.frappe_core.doctype.activity_log.activity_log import *
from frappe.frappe_core.doctype.module_profile.module_profile import *
from frappe.frappe_core.doctype.doctype_action.doctype_action import *
from frappe.frappe_core.doctype.rq_worker.rq_worker import *
from frappe.frappe_core.doctype.scheduled_job_type.scheduled_job_type import *
from frappe.frappe_core.doctype.audit_trail.audit_trail import *
from frappe.frappe_core.doctype.permission_log.permission_log import *
from frappe.frappe_core.doctype.deleted_document.deleted_document import *
from frappe.frappe_core.doctype.communication.communication import *
from frappe.frappe_core.doctype.scheduled_job_log.scheduled_job_log import *
from frappe.frappe_core.doctype.scheduler_event.scheduler_event import *
from frappe.frappe_core.doctype.has_domain.has_domain import *
from frappe.frappe_core.doctype.report.report import *
from frappe.frappe_core.doctype.logs_to_clear.logs_to_clear import *
from frappe.frappe_core.doctype.patch_log.patch_log import *