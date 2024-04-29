=================
Redrock scheduler
=================

.. image:: https://github.com/bigcrazyfrog/redrock_scheduler/actions/workflows/checks.yaml/badge.svg
   :target: https://github.com/bigcrazyfrog/redrock_scheduler/actions/
.. image:: https://github.com/bigcrazyfrog/redrock_scheduler/actions/workflows/deploy.yaml/badge.svg
   :target: https://github.com/bigcrazyfrog/redrock_scheduler/actions/

Setup localy
------------

.. code-block:: bash

    git clone https://github.com/bigcrazyfrog/redrock_scheduler.git

Create ``.env`` file from ``.env.example``.

Create docker images and execute the containers for development. Use commands from `Makefile`:

.. code-block:: bash

    make up
