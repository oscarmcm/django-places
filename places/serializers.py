from rest_framework import serializers
from decimal import Decimal, InvalidOperation
from . import Places

class PlacesSerializerField(serializers.Field):
    """
    Custom serializer field for handling a Places object.
    The expected input format for deserialization is a dictionary with keys 'country', 'city', 'latitude', 'longitude'.
    For serialization, it converts the Places object to this dictionary format.
    """

    def to_representation(self, value):
        """
        Converts the Places object to a dictionary for serialization.
        """
        if not value or not isinstance(value, Places):
            return None

        place_parts = value.place.split(', ')
        country = place_parts[1] if len(place_parts) > 1 else place_parts[0]
        city = place_parts[0] if len(place_parts) > 1 else ''

        return {
            'country': country,
            'city': city,
            'latitude': str(value.latitude),
            'longitude': str(value.longitude),
            'name': value.name
        }

    def to_internal_value(self, data):
        """
        Parses the incoming data and converts it into a Places object.
        """
        if not isinstance(data, dict):
            raise serializers.ValidationError("Expected a dictionary input for Places")

        country = data.get('country')
        if not isinstance(country, str) or not country:
            raise serializers.ValidationError({"country": "Country must be a non-empty string"})

        city = data.get('city')
        if not isinstance(city, str) or not city:
            raise serializers.ValidationError({"city": "City must be a non-empty string"})

        latitude = data.get('latitude')
        try:
            latitude = Decimal(latitude)
        except (ValueError, TypeError, InvalidOperation):
            raise serializers.ValidationError({"latitude": "Latitude must be a valid number"})

        longitude = data.get('longitude')
        try:
            longitude = Decimal(longitude)
        except (ValueError, TypeError, InvalidOperation):
            raise serializers.ValidationError({"longitude": "Longitude must be a valid number"})
        
        name = data.get('name')

        place = f"{country}, {city}" 
        return Places(place, latitude, longitude, name)
