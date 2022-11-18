"""
https://py2app.readthedocs.io/en/latest/

This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup, find_packages

from src import __version__

APP = ['src/main.py']

OPTIONS = {
    "iconfile": "resources/images/app.icns",
    "emulate_shell_environment": 1,
    "excludes": ['textblob'],
    "resources": ["resources", "scripts"],
}

setup(
    app=APP,
    version=__version__,
    packages=find_packages(include=['src', 'tests']),
    name="PodcastTool",
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    include_package_data=True,
)
