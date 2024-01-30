
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
        print('value from to_python', value)
        if isinstance(value, Places):
            return value
        
        if isinstance(value, list):
            if len(value) == 3:
                print('value', value)

        if value is None or isinstance(value, dict):
            return value

        # Assuming the value is a string representation of a dict
        # Convert it to a dict and then to a Places object
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
