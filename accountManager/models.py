from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import AbstractUser
from dataManager.models import *

class SiteUser(AbstractUser):
    # def save(self, *args, **kwargs):
        # If the user is being created
        # if self._state.adding:
        #     super().save(*args, **kwargs)  
        #     Profile.objects.create(user=self)  
        # else:
        #     super().save(*args, **kwargs)
	pass

class Profile(models.Model):
	user = models.OneToOneField(SiteUser, on_delete=models.CASCADE)

	displayName = models.CharField(max_length=150, default=user.name)
	profilePicture = models.ImageField(upload_to='files/profilePicture')
	bio = models.CharField(max_length=200)

	favoritedRoutes = models.ManyToManyField(Route, related_name='favoritedRoutes')
	completedRoutes = models.ManyToManyField(Route, related_name='completedRoutes')

