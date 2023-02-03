# [django-places](https://pypi.org/project/dj-places/)

[![PyPI](https://badge.fury.io/py/dj-places.png)](https://badge.fury.io/py/dj-places)

A Django app for store places with autocomplete function and a related map to the selected place.

## Quickstart
----------

Install `dj-places` and add it to your installed apps:

```
$ pip install dj-places
```

```
    INSTALLED_APPS = (
    	...
    	'places',
    	...
    )
```

Add the following settings and maps api key ([read more here](https://developers.google.com/maps/documentation/javascript/reference/map)):

```python
PLACES_MAPS_API_KEY='YourAwesomeUltraSecretKey'
PLACES_MAP_WIDGET_HEIGHT=480
PLACES_MAP_OPTIONS='{"center": { "lat": 38.971584, "lng": -95.235072 }, "zoom": 10}'
PLACES_MARKER_OPTIONS='{"draggable": true}'
```

## Usage
--------

Then use it in a project:

```python
from django.db import models
from places.fields import PlacesField


class MyLocationModel(models.Model):
    location = PlacesField()

```

This enables the following API:

```python
    >>> from myapp.models import ModelName
    >>> poi = ModelName.objects.get(id=1)
    >>> poi.position
    Place('Metrocentro, Managua, Nicaragua', 52.522906, 13.41156)
    >>> poi.position.place
    'Metrocentro, Managua, Nicaragua'
    >>> poi.position.latitude
    52.522906
    >>> poi.position.longitude
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

## Demo
------

![](http://g.recordit.co/LheQH0HDMR.gif)

### Credits
---------

Tools used in rendering this package:

*  [Cookiecutter](https://github.com/audreyr/cookiecutter)
*  [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
*  [jquery-geocomplete](https://github.com/ubilabs/geocomplete) (_no longer used in the project._)

### Similar Projects
------------

*  [Django Location Field](https://github.com/caioariede/django-location-field)
*  [Django GeoPosition](https://github.com/philippbosch/django-geoposition)

