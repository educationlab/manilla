# Manilla

Manilla aims to lower the barrier to writing beautiful, interactive, and high quality expository content for the web.

## Requirements
* PyGObject (``$ pip install pygobject``)
    * RSVG has been moved into GObjects Introspection, and thus PyGObject needs to be installed.
    * ``$ sudo apt-get install libgirespository1.0-dev gir1.2-rsvg-2.0 python3-cairo python-gi-cairo python3-gi``
* PyCairo (``$ pip install pycairo==1.11.0``)
    * For some reason, installing into an Anaconda environment doesn't work, and thus you need to use a virtualenv instead (``$ python -m venv <venv-name>``).

