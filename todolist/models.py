from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE will instruct Django to cascade the deleting effect
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    is_finished = models.BooleanField(default = False)

# source:
# https://docs.djangoproject.com/en/4.1/ref/models/fields/#foreignkey
# https://nsikakimoh.com/blog/auto_now-vs-auto_now_add-in-django
