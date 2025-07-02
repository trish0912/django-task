
import os
import django
import threading


os.environ.setdefault("DJANGO_SETTINGS_MODULE",'django_assessment.settings')
django.setup()


from test_2.models import Student

print(f"Caller running in thread: {threading.current_thread().name}")
Student.objects.create(name = "Samuel")