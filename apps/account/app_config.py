from django.apps import AppConfig


class AccountAppConfig(AppConfig):
    name = 'apps.account'

    def ready(self):
        import apps.account.listeners
