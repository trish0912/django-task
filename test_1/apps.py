from django.apps import AppConfig



class Test1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_1'

    def ready(self):
        import test_1.signals




