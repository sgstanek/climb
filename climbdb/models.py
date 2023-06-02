from django.db import models

class Location(models.Model):
    TYPE_CHOICES = [
        ('STE', 'State'),
        ('COU', 'Country'),
        ('ARE', 'Area'),
        ('WAL', 'Wall'),
        ('OTR', 'Other'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    location_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    parent_location = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='sub_locations')

class Route(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10) # use appropriate length
    description = models.TextField()
    picture = models.ImageField(upload_to='routes/')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='routes')