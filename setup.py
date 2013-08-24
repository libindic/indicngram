
#!/usr/bin/env python

from setuptools import setup, find_packages

name = "indicngram"

setup(
    name = name,
    version = "0.2",
    url = "http://silpa.org.in/NGram",
    license = "LGPL-3.0",
    description = "n-gram genereator for indic languages",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = """A n-gram generator for English, Hindi,
    Malayalam, Kannada and Bengali""",
    packages = find_packages(),
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools','indicsyllabifier'],
    zip_safe = False,
    )
