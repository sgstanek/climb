from django.urls import path
from . import views  # Import your app's views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include

app_name = 'accountManager'

urlpatterns = [
    path('profile/', views.profile, name='profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)