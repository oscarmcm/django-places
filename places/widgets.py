# -*- coding: utf-8 -*-
from django.forms import widgets
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from .conf import settings
from . import Places


class PlacesWidget(widgets.MultiWidget):
    template_name = 'places/widgets/places.html'

    def __init__(self, attrs=None):
        _widgets = (
            widgets.TextInput(
                attrs={'data-geo': 'formatted_address', 'data-id': 'map_place'}
            ),
            widgets.TextInput(
                attrs={
                    'data-geo': 'lat',
                    'data-id': 'map_latitude',
                    'placeholder': _('Latitude'),
                }
            ),
            widgets.TextInput(
                attrs={
                    'data-geo': 'lng',
                    'data-id': 'map_longitude',
                    'placeholder': _('Longitude'),
                }
            ),
            widgets.TextInput(attrs={'placeholder': 'Name', 'id': 'id_location_name'}),
            widgets.TextInput(attrs={'placeholder': 'Formatted Address', 'id': 'id_location_formatted_address'}),
            widgets.TextInput(attrs={'placeholder': 'Country', 'id': 'id_location_country'}),
            widgets.TextInput(attrs={'placeholder': 'City', 'id': 'id_location_city'}),
            widgets.TextInput(attrs={'placeholder': 'State', 'id': 'id_location_state'}),
            
        )
        super(PlacesWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if isinstance(value, str):
            return value.rsplit(',')
        if value:
            if isinstance(value, Places):
                value = value.to_dict()
            print('value from decompress', value)
            place = f'{value["country"]}, {value["city"]}, {value["formatted_address"]}'
            return [place, value["latitude"], value["longitude"], value["name"], value["formatted_address"], value["country"], value["city"], value["state"]]
        return [None, None]

    def get_context(self, name, value, attrs):
        context = super(PlacesWidget, self).get_context(name, value, attrs)
        context['map_widget_height'] = settings.MAP_WIDGET_HEIGHT
        context['map_options'] = settings.MAP_OPTIONS
        context['marker_options'] = settings.MARKER_OPTIONS

        return context

    class Media:
        js = (
            '//maps.googleapis.com/maps/api/js?key={}&libraries=places'.format(
                settings.MAPS_API_KEY
            ),
            'places/places.js',
        )
        css = {'all': ('places/places.css',)}
