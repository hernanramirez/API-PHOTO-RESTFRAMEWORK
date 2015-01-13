from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to='images', blank=False)
    address = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField('Latitude', default=0)
    longitude = models.FloatField('Latitude', default=0)
    upload_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Like(models.Model):
    user = models.ForeignKey(User)
    photo = models.ManyToManyField(Profile)
