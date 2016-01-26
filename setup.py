#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = '0.1.1'
DESCRIPTION = 'hassle free project switching'

setup(
    name='swproject',
    version=VERSION,
    description=DESCRIPTION,
    author='ybrs',
    license='MIT',
    url="https://github.com/ybrs/project-switcher",
    author_email='aybars.badur@gmail.com',
    packages=['swproject'],
    dependency_links = ['https://github.com/TomAnthony/itermocil/archive/master.zip#egg=itermocil-0.1.8'],
    install_requires = ['itermocil'],
    entry_points={
          'console_scripts': [
              'swproject = swproject.switcher:main'
          ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)