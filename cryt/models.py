from tokenize import blank_re
from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stylish_signature = models.ImageField(null=True, blank=True)
    text_signature = models.CharField(max_length=100)
    p12 = models.FileField()
    

    def __str__(self):
        return f"{self.user.email}"

class Document(models.Model):
    document = models.FileField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared', blank=True)
    signed = models.DateTimeField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, default="Mexico")

    def __str__(self):
        return f"{self.document}"
    
