from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    email = models.EmailField(max_length=225)
    date  = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.course}'
    