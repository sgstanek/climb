# Generated by Django 4.2.1 on 2023-06-04 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('picture', models.ImageField(default='default_image.jpg', upload_to='locations/')),
                ('location_type', models.CharField(choices=[('STE', 'State'), ('COU', 'Country'), ('ARE', 'Area'), ('WAL', 'Wall'), ('OTR', 'Other')], max_length=3)),
                ('parent_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_locations', to='dataManager.location')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='routes/')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='dataManager.location')),
            ],
        ),
    ]
