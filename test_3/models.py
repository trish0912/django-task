from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Attendence_Sheet(models.Model):
    note = models.TextField()

    def __str__(self):
        return self.note