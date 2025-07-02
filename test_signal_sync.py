
import time
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_assessment.settings')
django.setup()

from test_1.models import Student

start = time.time()
Student.objects.create(name='Mathew')
end = time.time()


print(f"Time taken for create(): {end - start:.2f} seconds")