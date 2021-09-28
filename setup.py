#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


readme = open('README.md').read()
history = open('CHANGELOG.md').read()

setup(
    author='Oscar Cortez',
    author_email='om.cortez.2010@gmail.com',
    name='dj-places',
    version='5.0.0',
    install_requires=['Django>=3.0'],
    python_requires='>=3',
    keywords='django geocomplete google maps places',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    description='A django app for store places using Google Maps API',
    license='MIT',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    url='https://github.com/oscarmcm/django-places',
    include_package_data=True,
    packages=find_packages(),
    package_data={
        'places': [
            'locale/*/LC_MESSAGES/*',
            'templates/places/widgets/*.html',
            'static/places/*',
        ],
    },
    project_urls={
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/oscarmcm',
        'Source': 'https://github.com/oscarmcm/django-places/',
        'Tracker': 'https://github.com/oscarmcm/django-places/issues',
    },
    zip_safe=False,
)
