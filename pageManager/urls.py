from django.urls import path

from . import views  # Import your app's views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Create a route for the index page of your app
    path('', views.index, name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)