# Generated by Django 4.2.1 on 2023-06-07 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountManager', '0005_profile_postedroutes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='postedRoutes',
        ),
    ]
