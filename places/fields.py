# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from decimal import Decimal

from django.db import models
from django.utils.six import with_metaclass
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

from . import Places
from .forms import PlacesField as PlacesFormField


class PlacesField(models.Field):
    description = _("A geoposition field (latitude and longitude)")

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

        matched = re.finditer(r'[-+]?\d*\.\d+|\d+', value)
        value_parts = [Decimal(x.group()) for x in matched]
        try:
            latitude = value_parts[0]
        except IndexError:
            latitude = '0.0'
        try:
            longitude = value_parts[1]
        except IndexError:
            longitude = '0.0'
        try:
            place = re.sub(r'[-+]?\d*\.\d+|\d+', '', value)[:-4]
        except:
            pass

        return Places(place, latitude, longitude)

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def get_prep_value(self, value):
        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return smart_text(value)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': PlacesFormField
        }
        defaults.update(kwargs)
        return super(PlacesField, self).formfield(**defaults)

