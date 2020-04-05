# Manilla

Manilla aims to lower the barrier to writing beautiful, interactive, and high quality expository content for the web.

## What is Manilla?
* Currently, it's difficult to publish high quality scientific and mathematical content on the web. There are certainly powerful libraries available, like KaTeX and  without fiddling around with libraries and

## Requirements
* **PyGObject**
    * RSVG has been moved into GObjects Introspection, and thus PyGObject needs to be installed.
    * Installation:
        ```
        $ sudo apt-get install libgirespository1.0-dev gir1.2-rsvg-2.0 python3-cairo python-gi-cairo python3-gi
        $ pip install pygobject
        ```
* **PyCairo**
    * For some reason, installing into an Anaconda environment doesn't work, and thus you need to use a virtualenv instead.
    * Installation:
        ```
        $ python -m venv <venv-name>
        $ pip install pycairo==1.11.0
        ```

## Docker
* A Docker container that enables the use of Manilla without any installation is coming soon, after the initial working prototypes are completed.

## Design Goals
* Manilla's initial goal is to support the chemistry packages from LaTeX in order to improve the quality of expository chemistry content on the web. Although there are powerful libraries available that render TeX for the web, there is generally a lack of support for packages that generate diagrams, which leads to a lack of well-maintained chemistry content on the web. Manilla leverages LaTeX to render these diagrams themselves and save them as SVGs which can then be rendered on the web.