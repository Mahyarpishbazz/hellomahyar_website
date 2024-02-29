from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class MyProjectData(models.Model):
    TitleForProject = models.CharField(max_length=50)
    BodyForText = models.TextField(max_length=150)
    ImageMyProject = models.ImageField(null=False, upload_to="assets/images")
    DateTime = models.DateTimeField(default=datetime.now, blank=True, editable=True)

    def __str__(self):
        return self.TitleForProject


class ContactBox(models.Model):
    FirstNameAndFamily = models.CharField(max_length=50, blank=True, null=True, default=None)
    Emails = models.CharField(max_length=150, blank=True, null=True, default=None)
    BodyText = models.TextField(max_length=500, blank=True, null=True, default=None)
    def __str__(self):
        return self.BodyText[:20]

