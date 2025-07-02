from django.apps import AppConfig


class Test3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_3'


    def ready(self):
        import test_3.signals
