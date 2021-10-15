#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

setup_requirements = ['pytest-runner']

setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='pytest plugin for chainmaker',
    long_description='pytest plugin for chainmaker',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'pytest-chainmaker', 'chainmaker', 'python-chainmaker'
    ],
    name='pytest-ini',
    packages=find_packages(include=['pytest_chainmaker']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/pytest-chainmaker',
    version='0.1',
    zip_safe=True,
    install_requires=[
        'pytest',
        'pytest-runner'
    ],
    entry_points={
        'pytest11': [
            'pytest-chainmaker = pytest_chainmaker.plugin',
        ]
    }
)
