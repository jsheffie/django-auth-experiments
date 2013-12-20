django-auth-experiments
=======================


**Some Experimenting with RESTApi's and Basic Authentication Headers**

**Author:** Jeff Sheffield.  [Follow me on Twitter](https://twitter.com/jeffsheffield).

Phase-One: Basic Auth RESTApi
========

* Create a django project.
* Build some simple data: link-farm data.
* Build a RESTApi to this data
* Build a [Requests](http://docs.python-requests.org/en/latest/) script to query the API
* Shoe-Horn in Apache
* Create some django-users.
* Create Basic-Authentication
* What Changes to we have to add to our Requests script to still gather data?

Installation Notes
==================

To clone the project from GitHub using git::

    git clone https://github.com/jsheffie/django-auth-experiments

To install django-auth-experiments in a virtualenvwrapper environment::

    cd django-auth-experiments 
    mkvirtualenv dj-auth
    workon dj-auth
    pip install -r docs/python_requirements.txt 
    pip install -r docs/python_optionals.txt 
    pip install -r docs/python_tut_requirements.txt 
    cdsitepackages
    ls


Optional Things
----------------
Im going to do a 'stream of consciousness' doc here: ( no-magic left behind )
Most of these things you are going to have from cloning the git repo so you can skip to 
'Run the server' if you feel so inclined.

Python is ready to go: now lets make a django project:

    cd django-auth-experiments
    django-admin.py newproject djauth

You now have a 'djauth' django project.

	├── djauth
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	└── manage.py

Lets create a app with some data.

	cd djauth
	python ./manage.py startapp linkfarm
	├── djauth
	│   ├── __init__.py
	│   ├── __init__.pyc
	│   ├── settings.py
	│   ├── settings.pyc
	│   ├── urls.py
	│   └── wsgi.py
	├── linkfarm
	│   ├── admin.py
	│   ├── __init__.py
	│   ├── models.py
	│   ├── tests.py
	│   └── views.py
	└── manage.py

TODO
----------------- 
figure out how to plug in with this.
https://github.com/fiee/generic_django_project

