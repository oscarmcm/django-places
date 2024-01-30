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

        # Initialize defaults
        place, latitude, longitude, name, formatted_address = (None, Decimal('0.0'), Decimal('0.0'), None, None)

        # Assign values based on the expected format
        if len(value_parts) >= 7:
            place = ','.join(value_parts[:2])  # Country and City
            try:
                latitude = Decimal(value_parts[2])
                longitude = Decimal(value_parts[3])
            except (ValueError, decimal.InvalidOperation):
                pass  # Keep default values if conversion fails

            name = value_parts[4]
            formatted_address = ', '.join(value_parts[5:])  # Address Line 1 and Line 2

        return Places(place, latitude, longitude, name, formatted_address)


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
