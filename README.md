# [django-places](https://pypi.org/project/dj-places/)

[![PyPI](https://badge.fury.io/py/dj-places.png)](https://badge.fury.io/py/dj-places)

A Django app for store places with autocomplete function and a related map to the selected place.

## Quickstart
----------

Install `dj-places` and add it to your installed apps:

```bash
$ pip install dj-places
```

```py
    INSTALLED_APPS = (
    	...
    	'places',
    	...
    )
```

Add djangorestframework to your installed apps (required for the package as it provide a serializer field):

```py
    INSTALLED_APPS = (
    	...
    	'rest_framework',
    	...
    )
```


Add the following settings and maps api key ([read more here](https://developers.google.com/maps/documentation/javascript/reference/map)):

```bash
PLACES_MAPS_API_KEY='YourAwesomeUltraSecretKey'
PLACES_MAP_WIDGET_HEIGHT=480
PLACES_MAP_OPTIONS='{"center": { "lat": 38.971584, "lng": -95.235072 }, "zoom": 10}'
PLACES_MARKER_OPTIONS='{"draggable": true}'
```

## Usage
--------

Then use it in a project:

```py
from django.db import models
from places.fields import PlacesField


class MyLocationModel(models.Model):
    location = PlacesField()

```

This enables the following API:

```bash
    >>> from myapp.models import MyLocationModel
    >>> poi = MyLocationModel.objects.get(id=1)
    >>> poi.location
    Place('Metrocentro, Managua, Nicaragua', 52.522906, 13.41156)
    >>> poi.location.place
    'Metrocentro, Managua, Nicaragua'
    >>> poi.location.latitude
    52.522906
    >>> poi.location.longitude
    13.41156
```

For using outside the Django Admin:

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
    {{ form.media }}
</form>
```
Remember to add the `{{ form.media }}` in your template.


For usage in Djangorestframework Serializers:

```py
from places.serializers import PlacesSerializerField
from rest_framework import serializers

class MyLocationModelSerializer(serializers.Serializer):
    location = PlaceSerializerField()
```

How the location data is displayed when doing a GET request in JSON with a serializer that has the field included, and is also how the data should be provided when doing a PUT/PATCH/POST:

```json
"location": {
    "city": "Stockholm",
    "country": "Sverige",
    "latitude": "59.32932349999999",
    "longitude": "18.0685808"
}
```

## Demo
------

![](http://g.recordit.co/LheQH0HDMR.gif)

### Credits
---------

Tools used in rendering this package:

*  [Cookiecutter](https://github.com/audreyr/cookiecutter)
*  [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
*  [jquery-geocomplete](https://github.com/ubilabs/geocomplete) (_no longer used in the project._)

Contributors
[minifisk](https://github.com/minifisk) - Adding serializer field

### Similar Projects
------------

*  [Django Location Field](https://github.com/caioariede/django-location-field)
*  [Django GeoPosition](https://github.com/philippbosch/django-geoposition)

