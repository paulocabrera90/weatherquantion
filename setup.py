#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()


requirements = [
    'Click>=6.0',
    'SQLAlchemy',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    name='wheaterquantion',
    version='0.1.0',
    description="command line utility",
    author="Paulo Cabrera",
    author_email='paulocabrera90@gmail.com',
  
    packages=[
        'wheaterquantion/',
        'wheaterquantion/core',
        'wheaterquantion/core/db',
        'wheaterquantion/core/galaxy',
        'wheaterquantion/core/geometry',
        'wheaterquantion/core/wheater',
        'wheaterquantion/core/wheater/job',
        'wheaterquantion/core/wheater/statistics',

    ],
    entry_points={
        'console_scripts': [
            'wheaterquantion=wheaterquantion.cli:main'
        ]
    },
    include_package_data=True,
    
    license="MIT license",
    zip_safe=False,
    keywords='wheaterquantion',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
 setup_requires=setup_requirements,
)
