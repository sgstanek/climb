# Generated by Django 4.2.1 on 2023-06-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManager', '0006_delete_picture_location_views_route_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_type', models.CharField(choices=[('l', 'Location'), ('r', 'Route')], max_length=1)),
                ('image', models.ImageField(upload_to='routes/')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='pictures',
            field=models.ManyToManyField(to='dataManager.picture'),
        ),
        migrations.AddField(
            model_name='route',
            name='pictures',
            field=models.ManyToManyField(to='dataManager.picture'),
        ),
    ]
