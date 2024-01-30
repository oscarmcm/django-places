# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
import decimal

from django.db import models
from django.utils.translation import gettext_lazy as _
try:
    from django.utils.encoding import smart_text
except ImportError:
    from django.utils.encoding import smart_str as smart_text

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
        if not value or value == 'None' or value == '':
            return None

        if isinstance(value, Places):
            return value

        # Split the value into parts and strip spaces
        value_parts = [val.strip() for val in value.split(',')]

        # Extract latitude and longitude
        try:
            latitude = Decimal(value_parts[-3])
            longitude = Decimal(value_parts[-2])
        except (IndexError, ValueError, decimal.InvalidOperation):
            # Default values in case of error
            latitude = Decimal('0.0')
            longitude = Decimal('0.0')

        # Extract place and name
        place = ','.join(value_parts[:-3]) if len(value_parts) > 3 else None
        name = value_parts[-1] if len(value_parts) > 3 else None

        return Places(place, latitude, longitude, name)


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
