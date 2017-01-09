# -*- coding: utf-8 -*-

from django import forms
from django.utils import six
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from .conf import settings


class PlacesWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs={'data-geo': 'formatted_address',}),
            forms.TextInput(attrs={'data-geo': 'lat',}),
            forms.TextInput(attrs={'data-geo': 'lng',}),
        )
        super(PlacesWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, six.text_type):
            return value.rsplit(',')
        if value:
            return [value.place, value.latitude, value.longitude]
        return [None, None]

    def format_output(self, rendered_widgets):
        return render_to_string('places/widgets/places.html', {
            'place': {
                'html': rendered_widgets[0],
                'label': _("place"),
            },
            'latitude': {
                'html': rendered_widgets[1],
                'label': _("latitude"),
            },
            'longitude': {
                'html': rendered_widgets[2],
                'label': _("longitude"),
            },
            'config': {
                'map_widget_height': settings.MAP_WIDGET_HEIGHT or 500,
                'map_options': settings.MAP_OPTIONS or '',
                'marker_options': settings.MARKER_OPTIONS or '',
            }
        })

    class Media:
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.0/jquery.min.js', # NOQA
            '//maps.googleapis.com/maps/api/js?key='+ settings.MAPS_API_KEY +'&libraries=places',  # NOQA
            '//cdnjs.cloudflare.com/ajax/libs/geocomplete/1.7.0/jquery.geocomplete.js',  # NOQA
            'places/places.js',
        )
        css = {
            'all': ('places/places.css',)
        }
