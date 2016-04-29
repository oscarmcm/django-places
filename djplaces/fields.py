# -*- coding: utf-8 -*-

from django.db.models import CharField
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_text

from . import Place
from .widgets import LocationWidget


class LocationField(CharField):
    description = _("A geoposition field (latitude and longitude)")

    def __init__(self, base_field=None, hide=False, *args, **kwargs):
        self.base_field = base_field
        kwargs['max_length'] = 63
        super(LocationField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(LocationField, self).deconstruct()
        del kwargs["max_length"]

        if self.base_field == '':
            raise ImproperlyConfigured()
        return name, path, args, kwargs

    def to_python(self, value):
        if not value or value == 'None':
            return None
        if isinstance(value, Place):
            return value
        if isinstance(value, list):
            return Place(value[0], value[1])

        # default case is string
        value_parts = value.rsplit(',')
        try:
            latitude = value_parts[0]
        except IndexError:
            latitude = '0.0'
        try:
            longitude = value_parts[1]
        except IndexError:
            longitude = '0.0'

        return Place(latitude, longitude)

    def get_prep_value(self, value):
        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return smart_text(value)

    def formfield(self, **kwargs):
        kwargs['widget'] = LocationWidget
        return super(LocationField, self).formfield(**kwargs)
