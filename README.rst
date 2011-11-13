Description
===========

This django application is for having a (beautiful) radiator view of all your jobs in Jenkins.

It can be customized for just see a certain view, so maybe it will be good for your customer or your global board.

.. image:: https://github.com/grigouze/django-jenkins-radiator/raw/master/screenshot.png

Set Up Instructions
===================

You Will Need
-------------

* A Jenkins CI Server (unless you want to add support for a different one).
* A web browser (Chrome or Firefox recommended - others not tested).

What To Do
----------
1. Update settings.py to add 'radiator' in INSTALLED_APPS, and add the import to settings_local
2. Update settings_local.py to point to your Jenkins CI server and the view of your jobs
3. Update urls.py for add the application 'radiator.urls'.
4. It's fini.
