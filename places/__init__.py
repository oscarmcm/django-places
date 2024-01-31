# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

default_app_config = 'places.apps.PlacesConfig'
__version__ = '5.2.1'


class Places(object):
    def __init__(self, place, latitude, longitude, name=None, formatted_address=None):

        if isinstance(latitude, float) or isinstance(latitude, int):
            latitude = str(latitude)
        if isinstance(longitude, float) or isinstance(longitude, int):
            longitude = str(longitude)

        self.place = place
        self.name = name 
        self.formatted_address = formatted_address
        self.latitude = Decimal(latitude)
        self.longitude = Decimal(longitude)

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.place, self.latitude, self.longitude, self.name, self.formatted_address)

    def __repr__(self):
        return "Places(%s)" % str(self)

    def __len__(self):
        return len(str(self))

    def __eq__(self, other):
        return (
            isinstance(other, Places)
            and self.latitude == other.latitude
            and self.longitude == other.longitude
        )

    def __ne__(self, other):
        return (
            not isinstance(other, Places)
            or self.latitude != other.latitude
            or self.longitude != other.longitude
        )
