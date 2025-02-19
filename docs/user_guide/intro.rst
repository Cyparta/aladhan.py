.. currentmodule:: aladhan

.. _intro:

Introduction
============

This is the documentation for ``aladhan.py``, an asynchronous pythonic wrapper for the Aladhan prayer times API.

Prerequisites
-------------

**Python 3.7 or higher is required.**


.. _installing:

Installing
----------

Install ``aladhan.py`` with pip:

.. tab:: Linux or MacOS

    .. code:: sh

        # fully install
        python3 -m pip install -U aladhan.py
        # only async requirements
        python3 -m pip install -U aladhan.py[async]
        # only sync requirements
        python3 -m pip install -U aladhan.py[sync]

.. tab:: Windows

    .. code:: sh

        # fully install
        py -3 -m pip install -U aladhan.py
        # only async requirements
        py -3 -m pip install -U aladhan.py[async]
        # only sync requirements
        py -3 -m pip install -U aladhan.py[sync]

.. _venv:

Virtual Environments
~~~~~~~~~~~~~~~~~~~~

Sometimes you want to keep libraries from polluting system installs or use a different version of
libraries than the ones installed on the system. You might also not have permissions to install libraries system-wide.
For this purpose, the standard library as of Python 3.3 comes with a concept called "Virtual Environment"s to
help maintain these separate versions.

A more in-depth tutorial is found on :doc:`py:tutorial/venv`.

However, for the quick and dirty:

1. Go to your project's working directory:

    .. tab:: Linux or MacOS

        .. code:: sh

            cd your-project-dir

    .. tab:: Windows

        .. code:: sh

            cd your-project-dir

2. Create a virtual environment:

    .. tab:: Linux or MacOS

        .. code:: sh

            python3 -m venv venv

    .. tab:: Windows

        .. code:: sh

            py -3 -m venv venv

3. Activate the virtual environment:

    .. tab:: Linux or MacOS

        .. code:: sh

            source venv/bin/activate

    .. tab:: Windows

        .. code:: sh

            venv\Scripts\activate.bat

4. Use pip like usual:

    .. tab:: Linux or MacOS

        .. code:: sh

            # fully install
            pip install -U aladhan.py
            # sync only
            pip install -U aladhan.py[sync]
            # async only
            pip install -U aladhan.py[async]

    .. tab:: Windows

        .. code:: sh

            # fully install
            pip install -U aladhan.py
            # sync only
            pip install -U aladhan.py[sync]
            # async only
            pip install -U aladhan.py[async]

Congratulations. You now have a virtual environment all set up.
You can start to code, learn more in :doc:`quickstart`.