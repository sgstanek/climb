import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'climb.settings')  # replace 'your_project.settings' with your actual settings
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from django.conf import settings

from dotenv import dotenv_values
from dotenv import load_dotenv, set_key



def setup():
    ENV_PATH = '.env'

    load_dotenv(ENV_PATH)
    google_client_id = input('Please enter the client_id: ')
    google_secret = input('Please enter the secret: ')

    site = Site.objects.get_or_create(name='localhost', domain='localhost')[0]
    settings.SITE_ID = site.id
    set_key(ENV_PATH, "LOCALHOST_ID", str(site.id))
    social_app = SocialApp.objects.get_or_create(
        provider='google', 
        name='google', 
        client_id=google_client_id,  # replace with your actual env vars
        secret=google_secret,  # replace with your actual env vars
    )[0]
    social_app.sites.add(site)  

if __name__ == "__main__":
    setup()