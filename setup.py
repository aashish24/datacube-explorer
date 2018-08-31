#!/usr/bin/env python3

from setuptools import find_packages, setup

import versioneer

tests_require = ["pylint", "digitalearthau", "requests-html"]

extras_require = {"test": tests_require}

setup(
    name="dea-dashboard",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    python_requires=">=3.6",
    url="https://github.com/data-cube/dea-dashboard",
    author="Geoscience Australia",
    packages=find_packages(),
    install_requires=[
        "cachetools",
        "click",
        "dataclasses",
        "datacube>=1.6",
        "flask",
        "fiona",
        "pyorbital",
        "geographiclib",
        "geoalchemy2",
        "simplekml",
        "structlog",
        "Flask-Caching",
        "gunicorn",
        "jinja2",
        "meinheld",
        "python-dateutil",
        "shapely",
    ],
    tests_require=tests_require,
    extras_require=extras_require,
)
