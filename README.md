django-auth-experiments
=======================


**Some Experimenting with RESTApi's and Basic Authentication Headers**

**Author:** Jeff Sheffield.  `Follow me on Twitter <https://twitter.com/jeffsheffield>`_.

Phase-One: Basic Auth RESTApi
========

* Create a django project.
* Build some simple data: link-farm data.
* Build a RESTApi to this data
* Build a `Requests <http://docs.python-requests.org/en/latest/>`_. script to query the API
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
    cd docs
    pip install -r docs/python_requirements.txt 
    pip install -r docs/python_optionals.txt 

