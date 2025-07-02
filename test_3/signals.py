from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, Attendence_Sheet


@receiver(post_save, sender=Student)
def student_post_save_handler(sender, instance, **kwargs):
    Attendence_Sheet.objects.create(note = f"Marked the attendence for {instance.name}")