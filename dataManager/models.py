from django.db import models
# from accountManager.models import Profile ## uncommenting breaks accountmanager due to circular importing :(

class Comment(models.Model):
    comment = models.TextField()
    # creator = models.ForeignKey(Profile)  ## uncommenting breaks accountmanager due to circular importing :(
    dateCreated = models.DateTimeField()
    likes = models.IntegerField(default=0)
    replies = models.ManyToManyField('self')

class Picture(models.Model):
    TYPE_CHOICES = [
        ('l', 'Location'),
        ('r', 'Route')
    ]

    image_type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    if image_type == 'l':
        image = models.ImageField(upload_to='locations/', default = 'default_image.jpg')
    else:
        image = models.ImageField(upload_to='routes/', default = 'default_image.jpg')
    
    likes = models.IntegerField(default=0)
    comments = models.ManyToManyField(Comment)

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
    pictures = models.ManyToManyField(Picture)
    location_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    parent_location = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='sub_locations')
    views = models.IntegerField(default=0)

class Route(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10) # use appropriate length
    description = models.TextField()
    pictures = models.ManyToManyField(Picture)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='routes')
    views = models.IntegerField(default=0)
