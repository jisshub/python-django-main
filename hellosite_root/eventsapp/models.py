from django.db import models
from datetime import datetime


# Create your models here.

class Venue(models.Model):
    venue_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    rate = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.venue_name


class Event(models.Model):
    event_name = models.CharField(max_length=30)
    date = models.DateField(default=datetime.now)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.CharField(max_length=20)
    attendees = models.IntegerField()

    def __str__(self):
        return self.event_name
