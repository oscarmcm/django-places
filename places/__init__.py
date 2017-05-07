# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

# Weird encoding python2 hack :'(
if sys.version_info < (3,0):
    reload(sys)
    sys.setdefaultencoding('utf8')

from decimal import Decimal

default_app_config = 'places.apps.PlacesConfig'
__version__ = '1.1.2'


class Places(object):

    def __init__(self, place, latitude, longitude):

        if isinstance(latitude, float) or isinstance(latitude, int):
            latitude = str(latitude)
        if isinstance(longitude, float) or isinstance(longitude, int):
            longitude = str(longitude)

        self.place = place
        self.latitude = Decimal(latitude)
        self.longitude = Decimal(longitude)

    def __str__(self):
        return "{0}, {1}, {2}".format(self.place, self.latitude, self.longitude)

    def __repr__(self):
        return "Places({0})".format(self)

    def __len__(self):
        return len(str(self))

    def __eq__(self, other):
        return isinstance(other, Places) and self.latitude == other.latitude and self.longitude == other.longitude

    def __ne__(self, other):
        return not isinstance(other, Places) or self.latitude != other.latitude or self.longitude != other.longitude
