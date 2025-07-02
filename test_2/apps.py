from django.apps import AppConfig


class Test2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_2'


    def ready(self):
        import test_2.signals