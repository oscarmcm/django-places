from rest_framework import serializers


class PlacesSerializerField(serializers.Field):
    """
    Custom serializer field for handling a Places object represented as a string.
    The expected format is "country,city,latitude,longitude".
    """

    def to_representation(self, value):
        """
        Converts the Places object to a dictionary for serialization.
        """
        if not value:
            return None

        parts = [part.strip() for part in str(value).split(',')]
        if len(parts) < 4:
            raise serializers.ValidationError("Invalid input format for Places")

        return {
            'country': parts[0],
            'city': parts[1],
            'latitude': parts[2],
            'longitude': parts[3]
        }

    def to_internal_value(self, data):
        """
        Parses the incoming data and converts it into a format suitable for the Places object.
        """
        if not isinstance(data, str):
            raise serializers.ValidationError("Expected a string input for Places")

        parts = [part.strip() for part in data.split(',')]
        if len(parts) != 4:
            raise serializers.ValidationError("Expected format: country,city,latitude,longitude")

        try:
            country, city, latitude, longitude = parts
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            raise serializers.ValidationError("Latitude and longitude must be valid numbers")

        return {
            'country': country,
            'city': city,
            'latitude': latitude,
            'longitude': longitude
        }
