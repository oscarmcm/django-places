from __future__ import unicode_literals

from django import forms
from django.utils.translation import gettext_lazy as _

from .widgets import PlacesWidget
from . import Places


class PlacesField(forms.MultiValueField):
    default_error_messages = {'invalid': _('Enter a valid geoposition.')}

    def __init__(self, *args, **kwargs):
        print("Initializing PlacesField with args:", args, "kwargs:", kwargs)

        kwargs.pop('encoder', None)
        kwargs.pop('decoder', None)

        fields = (
            forms.CharField(label=_('place')),
            forms.DecimalField(label=_('Latitude')),
            forms.DecimalField(label=_('Longitude')),
            forms.CharField(label=_('Name'), required=False),
            forms.CharField(label=_('Formatted Address'), required=False),
            forms.CharField(label=_('Country'), required=False),
            forms.CharField(label=_('City'), required=False),
            forms.CharField(label=_('State'), required=False),
        )
        if 'initial' in kwargs and kwargs['initial'] != '':
            kwargs['initial'] = Places(*kwargs['initial'].split(','))
        self.widget = PlacesWidget()
        super(PlacesField, self).__init__(fields, **kwargs)

    def widget_attrs(self, widget):
        classes = widget.attrs.get('class', '').split()
        classes.append('places')
        return {'class': ' '.join(classes)}

    def compress(self, value_list):
        print("Compressing values in PlacesField:", value_list)
        if value_list:
            return value_list
        return ""
    
    def prepare_value(self, value):
        print("Preparing value in PlacesField:", value)
        if isinstance(value, Places):
            return value.to_dict()
        return value
    

