# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from decimal import Decimal

__version__ = '1.0.0'


class Place(object):
    def __init__(self, latitude, longitude):
        if isinstance(latitude, float) or isinstance(latitude, int):
            latitude = str(latitude)
        if isinstance(longitude, float) or isinstance(longitude, int):
            longitude = str(longitude)

        self.latitude = Decimal(latitude)
        self.longitude = Decimal(longitude)

    def __str__(self):
        return "%s,%s" % (self.latitude, self.longitude)

    def __repr__(self):
        return "Place (%s)" % str(self)

    def __len__(self):
        return len(str(self))

    def __eq__(self, other):
        return isinstance(other, Place) and self.latitude == other.latitude and self.longitude == other.longitude  # NOQA

    def __ne__(self, other):
        return not isinstance(other, Place) or self.latitude != other.latitude or self.longitude != other.longitude  # NOQA
