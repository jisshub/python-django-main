from django.contrib import admin

# import models here
from .models import Event, Venue

# Register your models here.
admin.site.register(Event)
admin.site.register(Venue)
