==========
movesevent
==========

This is a django application  for the `Moves App (http://www.moves-app.com/) <http://www.moves-app.com/>`_.

.. image:: https://badge.fury.io/py/movesevent.png
    :target: http://badge.fury.io/py/movesevent

.. image:: https://pypip.in/d/movesevent/badge.png
        :target: https://crate.io/packages/movesevent/

        
Requirements
------------

* requests_
* moves_

.. _requests: http://docs.python-requests.org/en/latest/
.. _moves:  http://pypi.python.org/pypi/moves

Installation
------------

Install via pip:

.. code-block:: bash

    $ pip install movesevent

To enable `movesevent` in your project you need to add it to `INSTALLED_APPS` in your projects `settings.py` file:

.. code-block:: python

   INSTALLED_APPS = (
   ...
     'movesevent',
   ...
   )

and add this to `url.conf` file:

.. code-block:: python

   urlpatterns = patterns('',
   ...
       # Movesevent
    url(r'^mvevt/', include('movesevent.urls')),
   ...    
   )


The database synchronization is needed.


Usage
-----

The app provide 2 models:

  * MoveApp: It is an MovesApplication, so must provide client_id and secret
  * MoveUser: represent a move user associated to an app

.. figure:: https://github.com/francxk/movesevent/raw/master/doc/images/model.png
   :width: 1000  
  
Consult the `API documentation <https://dev.moves-app.com/docs/api>`_ for the methods supported by moves.

For each user


Disclaimer
----------

This library uses data from Moves but is not endorsed or certified by Moves. Moves is a trademark of ProtoGeo Oy.

License
-------

(The MIT License)

Copyright (c) 2013 [Franck Roudet]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.