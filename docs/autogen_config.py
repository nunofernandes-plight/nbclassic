#!/usr/bin/env python

from qtconsole.qtconsoleapp import JupyterQtConsoleApp

header = """\
.. _config:

Config
======

The notebook server can be run with a variety of command line arguments.
A list of available options can be found below in the :ref:`options section 
<options>`.

Defaults for these options can also be set by creating a file named
``jupyter_notebook_config.py`` in your Jupyter *profile folder*. The profile
folder is a subfolder of your Jupyter directory; to find out where it is
located, run::

  $ jupyter locate

To create a new set of default configuration files, with lots of information
on available options, use::

  $ jupyter profile create

.. seealso::

    :ref:`public_server`


.. _options:

Options
-------

This list of options can be generated by running the following and hitting 
enter::

  $ jupyter notebook --help

"""

with open("source/config.rst", 'w') as f:
    f.write(header)
    f.write(JupyterQtConsoleApp().document_config_options())
