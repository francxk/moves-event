#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 20 oct. 2013

@author: franck roudet
'''
from setuptools import setup, find_packages

current_version = '0.1'
component_name = 'moves_event'

setup(name='movesevent',
      version='0.1',
      description='Generate Django Moves Signal',
      author='Franck Roudet',
      author_email='anon@fr.fr',
      url='https://github.com/francxk/' + component_name,
      download_url='https://github.com/francxk/'+component_name+'/archive/V'+current_version + 'tar.gz',
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