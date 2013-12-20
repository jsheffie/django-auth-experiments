django-auth-experiments
=======================


**Some Experimenting with RESTApi's and Basic Authentication Headers**

**Author:** Jeff Sheffield.  [Follow me on Twitter](https://twitter.com/jeffsheffield).

Phase-One: Basic Auth RESTApi
========

- [x] Create a django project.
- [x] Build some simple data: [quickstart](http://django-rest-framework.org/tutorial/quickstart#project-setup)
- [ ] Build a RESTApi to this data
- [ ] Build a 'sample_client.py' [Requests](http://docs.python-requests.org/en/latest/) script to query the API
- [ ] Create some django-users.
- [ ] Create Basic-Authentication
- [ ] What Changes to we have to add to our Requests script to still gather data?
- [ ] Shoe-Horn in Apache
- [ ] Any Changes to our requests script?

Installation Notes
==================

To clone the project from GitHub using git:

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
	python ./manage.py startapp quickstart
	├── djauth
	│   ├── __init__.py
	│   ├── __init__.pyc
	│   ├── settings.py
	│   ├── settings.pyc
	│   ├── urls.py
	│   └── wsgi.py
	└── quickstart
	    ├── admin.py
	    ├── __init__.py
	    ├── models.py
	    ├── tests.py
	    └── views.py

- [*] Define some quickstart serializers, views and urls.
- [*] define sqlite dbms in configuration.
- [*] add quickstart, django_extensions, django-rest-framework into my INSTALLED_APPS.
- [*] Add REST_FRAMEWORK configuration settings for pagination.


	python ./manage.py syncdb
	python ./manage.py runserver localhost:8000

Testing our API
----------------

Web Browser

	GET:
	http://0.0.0.0:8000/
	http://0.0.0.0:8000/users/
	http://0.0.0.0:8000/users/1/
	http://0.0.0.0:8000/groups/
	http://0.0.0.0:8000/groups/1/


Curl

	curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/
	curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/ 
	curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/groups/ 

Observations
----------------
- [ ] Whats going on in the BASIC Authentication headers?




Dumping a fixture with data
----------------
	mkdir linkfarm/fixtures
	python ./manage.py dumpdata --format=json --indent=3 linkfarm > linkfarm/fixtures/initial_data.json



TODO
----------------- 
figure out how to plug in with this.
https://github.com/fiee/generic_django_project
or this


