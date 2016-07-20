# -*- coding: utf-8 -*-

from django import forms
from django.forms import widgets
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class LocationWidget(widgets.TextInput):

    def render(self, name, value, attrs=None):
        text_input = super(LocationWidget, self).render(name, value, attrs)

        return render_to_string('djplaces/map_widget.html', {
            'field_name': name,
            'field_input': mark_safe(text_input)
        })

    def _media(self):
        return forms.Media(
                    css={'all': ('css/djplaces.css',)},
                    js=(
                        '//maps.googleapis.com/maps/api/js?key='+ settings.MAPS_API_KEY +'&libraries=places',  # NOQA
                        'js/djplaces.js',
                        '//cdnjs.cloudflare.com/ajax/libs/geocomplete/1.7.0/jquery.geocomplete.min.js'  # NOQA
                        )
                )
    media = property(_media)
