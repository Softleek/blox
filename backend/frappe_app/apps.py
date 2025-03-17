from django.apps import AppConfig


class FrappeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frappe_app'

    def ready(self):
        import core.signals
        # import frappe_app.signals
