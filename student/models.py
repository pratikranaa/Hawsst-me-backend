# student/models.py  

from django.db import models
from authentication.models import User

class Student(models.Model):
    # other fields related to student ...
    student_id = models.CharField(max_length=10, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_account")