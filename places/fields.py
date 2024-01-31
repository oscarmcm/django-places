
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from decimal import Decimal
import decimal

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField

try:
    from django.utils.encoding import smart_text
except ImportError:
    from django.utils.encoding import smart_str as smart_text

from . import Places
from .forms import PlacesField as PlacesFormField


class PlacesField(JSONField):
    description = _('A geoposition field (latitude and longitude)')

    def __init__(self, *args, **kwargs):
        super(PlacesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, Places):
            return value

        # Check if value is a string representation of a list
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except (ValueError, TypeError):
                pass  # If it's not a JSON string, proceed with the original value

        if isinstance(value, list):
            # Process list to create a Places object
            if len(value) >= 8:
                return Places(
                    country=value[5],
                    city=value[6],
                    state=value[7],
                    latitude=value[1],
                    longitude=value[2],
                    name=value[3],
                    formatted_address=value[4]
                )

        if value is None or isinstance(value, dict):
            return value

        # Handle string representation of a dict
        try:
            value_dict = json.loads(value)
            return Places.from_dict(value_dict)
        except (ValueError, TypeError):
            # In case the string cannot be converted to a dict
            return None

    def get_prep_value(self, value):
        if isinstance(value, Places):
            return value.to_dict()

        # If the value is already a dict or None, just use it as-is
        return value
    
    def clean(self, value, model_instance):
        return value

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.to_python(value)

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return smart_text(value)

    def formfield(self, **kwargs):
        defaults = {'form_class': PlacesFormField}
        defaults.update(kwargs)
        return super(PlacesField, self).formfield(**defaults)
