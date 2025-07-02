from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
import threading


@receiver(post_save, sender=Student)
def student_post_save_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")
