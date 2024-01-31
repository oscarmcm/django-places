from rest_framework import serializers
from decimal import Decimal, InvalidOperation
from . import Places

class PlacesSerializerField(serializers.Field):
    """
    Custom serializer field for handling a Places object.
    The expected input format for deserialization is a dictionary with keys 'country', 'city', 'latitude', 'longitude'.
    For serialization, it converts the Places object to this dictionary format.
    """

    def to_representation(self, obj):
        if isinstance(obj, Places):
            return obj.to_dict()
        elif isinstance(obj, dict):
            return obj
        else:
            return None
    
    def to_internal_value(self, data):
        place_from_dict =  Places.from_dict(data)
        return place_from_dict
