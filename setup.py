#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 20 oct. 2013

@author: franck roudet
'''
from setuptools import setup, find_packages


setup(name='movesevent',
      version='0.1',
      description='Generate Django Moves Signal',
      author='Franck Roudet',
      author_email='anon@fr.fr',
      url='https://github.com/l',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      package_data={'': ['LICENSE', 'NOTICE'],},
      install_requires=open('requirements.txt').read(),
      long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      include_package_data=True,
      license=open('LICENSE.txt').read(),
      zip_safe=False,
      )