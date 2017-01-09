from django.db import models

from places.fields import PlacesField


class Place(models.Model):
    location = PlacesField(blank=True)

    def __unicode__(self):
        return self.location.place

    def __str__(self):
        return self.__unicode__()
