from django.test import TestCase

from rest_framework import serializers

from places.serializers import PlacesSerializerField



class PlaceSerializerFieldRepresentation(TestCase):

    def setUp(self):
        self.field = PlacesSerializerField()

    def test_valid_representation(self):
        valid_input = "USA,New York,40.7128,-74.0060"
        expected_output = {
            'country': 'USA',
            'city': 'New York',
            'latitude': '40.7128',
            'longitude': '-74.0060'
        }
        self.assertEqual(self.field.to_representation(valid_input), expected_output)

    def test_invalid_representation(self):
        invalid_input = "Incomplete data"
        with self.assertRaises(serializers.ValidationError):
            self.field.to_representation(invalid_input)

    def test_null_representation(self):
        null_input = None
        self.assertIsNone(self.field.to_representation(null_input))



class TestPlaceSerializerFieldToInternalValue(TestCase):
    def setUp(self):
        self.field = PlacesSerializerField()

    def test_valid_input(self):
        input_data = "USA,New York,40.7128,-74.0060"
        expected_output = {
            'country': 'USA',
            'city': 'New York',
            'latitude': 40.7128,
            'longitude': -74.0060
        }
        self.assertEqual(self.field.to_internal_value(input_data), expected_output)

    def test_invalid_input(self):
        invalid_data = "Incomplete data"
        with self.assertRaises(serializers.ValidationError):
            self.field.to_internal_value(invalid_data)

    def test_null_input(self):
        null_input = None
        with self.assertRaises(serializers.ValidationError):
            self.field.to_internal_value(null_input)