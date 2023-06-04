from django.contrib import admin

# Register your models here.
from accountManager.models import *
admin.site.register(Profile, SiteUser)
