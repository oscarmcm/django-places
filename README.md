
django-places
=============================

A Django app for store places with autocomplete function and a related map to the selected place.

Badges
---------

[![PyPI](https://badge.fury.io/py/dj-places.png)](https://badge.fury.io/py/dj-places)
[![Travis-ci](https://travis-ci.org/oscarmcm/django-places.png?branch=master)](https://travis-ci.org/oscarmcm/django-places)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d6433fc7fc384f63b9f41fc251ee70b1)](https://www.codacy.com/app/om-cortez-2010/django-places?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=oscarmcm/django-places&amp;utm_campaign=Badge_Grade)

Quickstart
----------

Install dj-places and add it to your installed apps:

    $ pip install dj-places

    INSTALLED_APPS = (
    	...
    	'djplaces',
    	...
    )

Add in your project settings the following values:

	JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js'
 	GEOCOMPLETE_URL = '//cdnjs.cloudflare.com/ajax/libs/geocomplete/1.7.0/jquery.geocomplete.min.js'
 	GOOGLE_PLACES_URL = '//maps.googleapis.com/maps/api/js?libraries=places'


Then use it in a project:

    from djplaces.fields import LocationField
    place = models.CharField(max_length=250)
    location = LocationField(base_field='place')

TODO-LIST
--------

* [ ] Write some test ASAP!
* [ ] Support Inline Admin
* [ ] Use Django Admin Jquery
* [ ] Set custom zoom map value
* [ ] Custom property for lat and lng values

Running Tests
--------------

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Special thanks to [Helmy Giacoman](https://github.com/eos87) for motivating me to make this package.

Tools used in rendering this package:

*  [Cookiecutter](https://github.com/audreyr/cookiecutter)
*  [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
*  [jquery-geocomplete](https://github.com/ubilabs/geocomplete)

Similar Projects
------------

*  [Django Location Field](https://github.com/caioariede/django-location-field)
*  [Django Geoposition](https://github.com/philippbosch/django-geoposition)
