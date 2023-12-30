from django.test import TestCase
from rest_framework import serializers
from places.serializers import PlacesSerializerField
from places.fields import Places  

class PlaceSerializerFieldRepresentation(TestCase):
    def setUp(self):
        self.field = PlacesSerializerField()

    def test_valid_representation(self):
        valid_places = Places("USA, New York", "40.7128", "-74.0060")
        expected_output = {
            'country': 'USA',
            'city': 'New York',
            'latitude': '40.7128',
            'longitude': '-74.0060'
        }
        self.assertEqual(self.field.to_representation(valid_places), expected_output)

    def test_invalid_representation(self):
        invalid_places = "Incomplete data"  # This should be an invalid type
        result = self.field.to_representation(invalid_places)
        self.assertIsNone(result)

    def test_null_representation(self):
        null_input = None
        self.assertIsNone(self.field.to_representation(null_input))

class TestPlaceSerializerFieldToInternalValue(TestCase):
    def setUp(self):
        self.field = PlacesSerializerField()

    def test_valid_input(self):
        input_data = {
            'country': 'USA',
            'city': 'New York',
            'latitude': '40.7128',
            'longitude': '-74.0060'
        }
        expected_output = Places("USA, New York", 40.7128, -74.0060)
        result = self.field.to_internal_value(input_data)
        self.assertEqual(result.place, expected_output.place)
        self.assertEqual(result.latitude, expected_output.latitude)
        self.assertEqual(result.longitude, expected_output.longitude)

    def test_invalid_input_missing_fields(self):
        invalid_data = {"country": "USA"}  # Missing other fields
        with self.assertRaises(serializers.ValidationError):
            self.field.to_internal_value(invalid_data)

    def test_invalid_input_wrong_types(self):
        invalid_data = {
            'country': 'USA',
            'city': 'New York',
            'latitude': 'not_a_number',
            'longitude': '-74.0060'
        }
        with self.assertRaises(serializers.ValidationError):
            self.field.to_internal_value(invalid_data)

    def test_null_input(self):
        null_input = None
        with self.assertRaises(serializers.ValidationError):
            self.field.to_internal_value(null_input)
