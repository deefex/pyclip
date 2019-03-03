# -*- coding: utf-8 -*-
from setuptools import setup

from pyclip import __version__, __author__


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='pyclip',
    version=__version__,
    description='Pyclip - Counterstring Generator',
    long_description=read("README.md"),
    author=__author__,
    author_email='',
    url='https://github.com/deefex/pyclip',
    install_requires=open('requirements.txt').readlines(),
    license=read("LICENSE"),
    zip_safe=False,
    include_package_data=True,
    keywords='pyclip',
    packages=['pyclip'],
    entry_points={
        'console_scripts': [
            "pyclip=pyclip.pyclip:main"
        ]
    },
)
