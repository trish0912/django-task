from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
import time


@receiver(post_save, sender=Student)
def create_student(sender, instance, created, **kwargs):
    print("Signal started")
    time.sleep(5) #some processing going here
    print("Signal finished")