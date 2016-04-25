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
                        settings.JQUERY_URL,
                        settings.GOOGLE_PLACES_URL,
                        settings.GEOCOMPLETE_URL,
                        'js/djplaces.js'
                        )
                )
    media = property(_media)

