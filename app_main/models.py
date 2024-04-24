from django.db import models

from app_users.models import Student


class Book(models.Model):
    student = models.OneToOneField(to=Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.title}"
