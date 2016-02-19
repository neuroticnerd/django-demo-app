
Demo Django Application
============================

Local Development Setup
-------------------------

After cloning the repo, you will want to ``cd`` to the root of the project
and create a new virtualenv:

.. code:: shell

    mkvirtualenv djangodemo

Then you will need to install the project requirements:

.. code:: shell

    pip install -r requirements.txt

The database needs to be configured and a default user and site loaded:

.. code:: shell

    python manage.py migrate
    python manage.py loaddata initial_fixture.json

After that has completed you will be able to run the dev server via:

.. code:: shell

    python manage.py runserver --insecure

The ``--insecure`` flag ensures that static content will be served even if you
set ``DEBUG=False`` since it is not currently setup to serve static content
from an alternative source.

You should now be able to login as:
*   username=``admin``
*   password=``superuser``

There are a number of environment variables which you can set that will
be read into the ``settings.py`` file to modify runtime behavior:

*   ``DJANGO_DEMO_SITE_ID``: will populate the ``SITE_ID`` setting

*   ``DJANGO_DEMO_DEBUG``: will be read into the Django ``DEBUG`` setting

*   ``DJANGO_DEMO_TEMPLATE_DEBUG``: will be read into the Django ``TEMPLATE_DEBUG`` setting

*   ``DJANGO_DEMO_SECRET_KEY``: will be read into the ``SECRET_KEY`` setting

*   ``DJANGO_DEMO_STATIC_ROOT``: populates the ``STATIC_ROOT`` setting

*   ``DJANGO_DEMO_MEDIA_ROOT``: populates the ``MEDIA_ROOT`` setting




Chosen Project
----------------

2.  Create a Django project with an action-tracking application. The goal of
the application is to store/manage actions. A user should be able to create,
change, and delete actions. Actions can be assigned to any user. Actions should
have at least a title and a description, and they should be capable of being
displayed as a group in some fashion relative to the current month.

Unfortunately, I didn't have nearly as much time as I had planned for to work
on this; due to the double-holiday weekend I wasn't able to even start until
Tuesday. Then wednesday I had to drive down to my folks place to tend to some
family matters with my grandfather. So between the two of those things I only
had approx. three to three and a half days of time to actually invest in this,
I had not anticipated this week being as hectic as it has been.


Things I Would Do Differently
---------------------------------

Given more time to flesh out the project a bit, there are a good number of
things I would want to enhance or take a different approach to. The most
notable things might be the absence of proper documentation and pytests. I
wanted to make sure the functionality existed first, but then due to the
limited availability of time to work on the project, I wasn't able to go back
and add unit tests and some proper docstrings.

The next thing which is absent is a ``vagrantfile``. I normally use Vagrant
and VirtualBox for local development environments since it makes it
exponentially easier for someone unfamiliar with the project to get up and
running much faster. I do know that Hashicorp has released a successor to
Vagrant now, but I've not had time yet to investigate and get up to speed.

I would replace
SQLite as the database backend with PostgreSQL for any sort of production
environment. Redis is my prefered caching software due to its performance,
ease of use, and excellent third party packages available; aside from being
a great key-value store in general, it is my preferred Django sessions backend.
Storing media uploads or collected static files on disk on the server instance
itself is typically something I avoid; I feel it is much better to let AWS S3
and their CDN handle serving static content. Replacing the static files
backend with a 3rd party S3 connector in the Django settings has (in my
experience at least) been a fairly painless way to store static files.

A good number of the things I have mentioned above are predicated on the
assumption that most production sites would have multiple application servers
behind routing/load balancing making things like storing sessions or static
content on the instance infeasible to begin with.

The way the CRUD for Actions is currently setup, it uses what is available
natively to Django, however, it should really be implemented as more of a
true REST API utilizing something like TastyPie or django-rest-framework
which would then be accessed via AJAX from the client side.

The way that the lists of actions are used currently, it would become quite
unwieldy without pagination as soon as the number of actions started growing.
Django has easy ways of adding pagination but unfortunately I have not yet
had time to add it into the project.

Lastly, it should really have a method included for easily doing repeatable,
idempotent deployments. I like Ansible for this task, and that's what I always
use when given the choice. It has the benefit of being agent-less and operating
over SSH which increases security.
