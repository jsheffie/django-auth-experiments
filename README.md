django-auth-experiments
=======================


**Some Experimenting with RESTApi's and Basic Authentication Headers**

The point here is to get to write some in-depth requsts scripts. While getting to know
the details of both sides of the house. Server-and-Client.

This was done in a very community oriented way: First I started with the
rest_framework [quickstart](http://django-rest-framework.org/tutorial/quickstart#project-setup)
app. Then I followed the rest_framework tutorial a bit futher and did the [pastbin](http://django-rest-framework.org/tutorial/1-serialization) syntax highlighter. I followed this all up by writting a *sample_client.py* using python's [Requests](http://docs.python-requests.org/en/latest/) library.

Futhermore I explored the authentication headers that are passed two and from the server with BASIC Authtentiation

**Narrator:** Jeff Sheffield.  [Follow me on Twitter](https://twitter.com/jeffsheffield).

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

Terminal 1:

	python ./manage.py runserver 0.0.0.0:8000

Web Browser

	GET:
	http://0.0.0.0:8000/
	http://0.0.0.0:8000/users/
	http://0.0.0.0:8000/users/1/
	http://0.0.0.0:8000/groups/
	http://0.0.0.0:8000/groups/1/
	http://0.0.0.0:8000/groups/1/?format=json


Curl

	curl -X GET -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/
	curl -X GET -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/ 
	curl -X GET -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/groups/ 

Writing the Request's client
----------------

	utils/sample_client.py

Observations
----------------
- [*] Whats going on in the BASIC Authentication headers?

So first, go low:
I modified the 'sample_client.py' script to only request '/users/'. I made sure that my rest_framework server code view: UserViewSet class has the 'permission_classes' set to 'IsAuthenticated' thus requiring authentication for this resource.

I modified 'sample_client.py' to try to first request the resource without any authentication.
Then follow that up with a BasicAuthentication request if the first one fails with any status
code other thant 200.

I fired up wireshark and listed on the loopback interface. Then filtered for tcp.port == 8000. This got the ball rollowing. 

So what happened?

I realized that the server is passing back a On the first unauthenticated request.
The server responds with http/1.0 header HTTP_STATUS_CODE: 403 Forbidden

Then the client reqsonds with *Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==* just as described in this [Basic Authentication](http://en.wikipedia.org/wiki/Basic_access_authentication) wiki.

However this sucks... I feel like I am really missing the picture here. This is hard to see and debug.

I was not able to get: [httpbin](http://httpbin.org/) wired in the way I expected to be able too.

Wire in some django middleware to display the header.
----------------
We have all of this data in the django framework, how hard would it be to print it? or log it to a file. 'djauth/quickstart/middleware/logging.py' 
Note: this is not a production type of thing you want to run.







Dumping a fixture with data
----------------
	mkdir linkfarm/fixtures
	python ./manage.py dumpdata --format=json --indent=3 linkfarm > linkfarm/fixtures/initial_data.json



TODO
----------------- 
figure out how to plug in with this.
https://github.com/fiee/generic_django_project
or this

References
----------------- 
* [httpbin](http://httpbin.org/)
* [Requests](http://docs.python-requests.org/en/latest/)
* [Basic Authentication](http://en.wikipedia.org/wiki/Basic_access_authentication)

