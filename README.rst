=============================
django-places
=============================

.. image:: https://badge.fury.io/py/dj-places.png
    :target: https://badge.fury.io/py/dj-places

.. image:: https://travis-ci.org/oscarmcm/dj-places.png?branch=master
    :target: https://travis-ci.org/oscarmcm/django-places

A django app for store places with autocomplete and a related map

Quickstart
----------

Install dj-places and add it to your installed apps::

    $ pip install dj-places

    INSTALLED_APPS = (
    	...
    	'djplaces',
    	...
    )

Add in your project settings the following values::

	JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js'
 	GEOCOMPLETE_URL = '//cdnjs.cloudflare.com/ajax/libs/geocomplete/1.7.0/jquery.geocomplete.min.js'>
 	GOOGLE_PLACES_URL = '//maps.googleapis.com/maps/api/js?libraries=places''


Then use it in a project::

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

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Special thanks to [Helmy Giacoman](https://github.com/eos87) for motivating me to make this package.

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_
*  jquery-geocomplete_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _jquery-geocomplete_: https://github.com/ubilabs/geocomplete