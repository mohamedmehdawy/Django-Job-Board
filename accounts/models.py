from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    city = models.ForeignKey('City', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="profile/")

    def __str__(self):
        return str(self.user)

class City(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)