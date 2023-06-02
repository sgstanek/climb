from django.contrib import admin

# Register your models here.
from dataManager.models import Location, Route

admin.site.register(Location)
admin.site.register(Route)
