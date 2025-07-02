import os
import django
from django.db import transaction

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_assessment.settings")
django.setup()


from test_3.models import Student, Attendence_Sheet

# Clean any previous attendence_sheet
Attendence_Sheet.objects.all().delete()

try:
    with transaction.Atomic():
        Student.objects.create(name="Sam Mathews")
        raise Exception("Forced failure to simulate rollback")
    
except:
    print("Transaction rolled back")

# Check whether the signal’s attendence_sheet was created
note_exists = Attendence_Sheet.objects.filter(note__icontains="Sam Mathews").exists()

if note_exists:
    print("Signal effects not rolled back")
else:
    print("Signal effect rolled back.(proof that signal shares transanction)")
