from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    p12 = models.FileField()
    

    def __str__(self):
        return f"{self.user.email}"

class Document(models.Model):
    document = models.FileField()
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared', blank=True)

    def __str__(self):
        return f"{self.document}"
    