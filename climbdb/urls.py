from django.urls import path

from . import views  # Import your app's views

urlpatterns = [
    # Create a route for the index page of your app
    path('', views.index, name='index'),
]
