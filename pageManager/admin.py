from django.contrib import admin

# Register your models here.
from .models import Location, Route

admin.site.register(Location)
admin.site.register(Route)