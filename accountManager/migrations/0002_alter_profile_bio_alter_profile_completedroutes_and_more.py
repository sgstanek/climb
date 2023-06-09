# Generated by Django 4.2.1 on 2023-06-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManager', '0001_initial'),
        ('accountManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='completedRoutes',
            field=models.ManyToManyField(blank=True, related_name='completedRoutes', to='dataManager.route'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='displayName',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favoritedRoutes',
            field=models.ManyToManyField(blank=True, related_name='favoritedRoutes', to='dataManager.route'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to='files/profilePicture'),
        ),
    ]
