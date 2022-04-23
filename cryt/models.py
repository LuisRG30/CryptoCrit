from tokenize import blank_re
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.files.base import ContentFile, File

from django.contrib.auth.models import User

from .KeyGenerator import KeyGenerator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    stylish_signature = models.ImageField(null=True, blank=True)
    text_signature = models.CharField(max_length=100, null=True, blank=True)
    private_key= models.FileField(null=True, blank=True)
    public_key = models.FileField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.user.username}"

class Document(models.Model):
    document = models.FileField(null=True)
    signature = models.FileField(null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared', blank=True)
    signed = models.DateTimeField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, default="Mexico")

    def __str__(self):
        return f"{self.document}"

class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    operation = models.CharField(max_length=400)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.owner} -- {self.operation}"

    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        k = KeyGenerator()
        with open('privatekey', 'wb+') as f:
            f.write(k.privkey.save_pkcs1('PEM'))
            instance.profile.private_key.save('privatekey.key', File(f))

        with open('publickey', 'wb+') as f:
            f.write(k.pubkey.save_pkcs1('PEM'))
            instance.profile.public_key.save('publickey.key', File(f))

    instance.profile.save()

post_save.connect(create_user_profile, sender=User)