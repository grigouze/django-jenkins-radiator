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
