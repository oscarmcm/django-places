# -*- coding: utf-8 -*-

from django.db.models import CharField
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from .widgets import LocationWidget


class LocationField(CharField):
    description = _("A geoposition field (latitude and longitude)")

    def __init__(self, verbose_name=None, name=None,
                 base_field=None, *args, **kwargs):
        self.verbose_name = verbose_name
        self.name = name
        self.base_field = base_field
        kwargs['max_length'] = 63
        super(LocationField, self).__init__(
            verbose_name, name, *args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(LocationField, self).deconstruct()
        del kwargs["max_length"]

        if self.base_field == '':
            raise ImproperlyConfigured()
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        kwargs['widget'] = LocationWidget
        return super(LocationField, self).formfield(**kwargs)
