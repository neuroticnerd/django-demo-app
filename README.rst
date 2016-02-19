
Demo Django Application
============================

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
had approx. three to three and a half days of time to actually invest in this.


Things I Would Do Differently
---------------------------------

Given more time to flesh out the project a bit, there are a good number of
things I would want to enhance or take a different approach to. The most
notable things might be the absence of proper documentation and pytests. I
wanted to make sure the functionality existed first, but then due to the
limited availability of time to work on the project, I wasn't able to go back
and add unit tests and some proper docstrings.

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


Required Environment Variables
--------------------------------

*   ``DJANGO_DEMO_DEBUG``: will be read into the Django ``DEBUG`` setting
*   ``DJANGO_DEMO_SECRET_KEY``: will be read into the ``SECRET_KEY`` setting
