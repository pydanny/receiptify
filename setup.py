#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os
import sys

import receiptify


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (
            receiptify.__version__, receiptify.__version__))
    print("  git push --tags")
    sys.exit()

LONG_DESCRIPTION = open('README.rst').read()
HISTORY = open('HISTORY.rst').read()

setup(
    name='receiptify',
    version=receiptify.__version__,
    description="Uses complexity and simplicity to generate receipts.",
    long_description=LONG_DESCRIPTION + '\n\n' + HISTORY,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup"
    ],
    keywords='python,json',
    author=receiptify.__author__,
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/receiptify',
    license='MIT',
    py_modules=['receiptify', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
            'complexity',
            'simplicity'
        ],
    entry_points={
        'console_scripts': [
            'receiptify=receiptify:command_line_runner',
        ]
    },
)

# (*) Please direct queries to Github issue list, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.
