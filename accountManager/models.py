from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import AbstractUser
from dataManager.models import *
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

	
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	displayName = models.CharField(max_length=150, blank=True, null=True)
	profilePicture = models.ImageField(upload_to='files/profilePicture',blank=True, null=True)
	bio = models.CharField(max_length=200,blank=True, null=True)

	favoritedRoutes = models.ManyToManyField(Route, related_name='favoritedRoutes',blank=True)
	completedRoutes = models.ManyToManyField(Route, related_name='completedRoutes',blank=True)

@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    Profile.objects.create(user=user, displayName=user.username)
