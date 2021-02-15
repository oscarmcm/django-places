# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.db import models
from django.utils.encoding import smart_text
from django.utils.translation import gettext_lazy as _

from . import Places
from .forms import PlacesField as PlacesFormField


class PlacesField(models.Field):
    description = _('A geoposition field (latitude and longitude)')

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        super(PlacesField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def to_python(self, value):
        if not value or value == 'None':
            return None
        if isinstance(value, Places):
            return value
        if isinstance(value, list):
            return Places(value[0], value[1], value[2])

        value_parts = [Decimal(val) for val in value.split(',')[-2:]]

        try:
            latitude = value_parts[0]
        except IndexError:
            latitude = '0.0'

        try:
            longitude = value_parts[1]
        except IndexError:
            longitude = '0.0'
        try:
            place = ','.join(value.split(',')[:-2])
        except:
            pass

        return Places(place, latitude, longitude)

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        return str(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return smart_text(value)

    def formfield(self, **kwargs):
        defaults = {'form_class': PlacesFormField}
        defaults.update(kwargs)
        return super(PlacesField, self).formfield(**defaults)
