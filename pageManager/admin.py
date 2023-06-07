from django.contrib import admin

# Register your models here.
from dataManager.models import Location, Route, Picture

admin.site.register(Location)
admin.site.register(Picture)
admin.site.register(Route)
