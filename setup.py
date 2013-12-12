#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 20 oct. 2013

@author: franck roudet
'''
from setuptools import setup, find_packages
import os

PROJECT_ROOT = os.environ.get('OPENSHIFT_REPO_DIR', os.path.dirname(os.path.abspath(__file__)))

current_version = '0.1.0'
component_name = 'moves-event'

setup(name=component_name,
      version=current_version,
      description='Generate Django Moves Signal',
      author='Franck Roudet',
      author_email='anon@fr.fr',
      url='https://github.com/francxk/' + component_name + '/',
      #download_url='https://github.com/francxk/'+component_name+'/archive/v'+current_version + '.tar.gz',
      download_url='https://github.com/francxk/'+component_name+'/archive/' + 
      component_name+ '-' +current_version + '.tar.gz',
      #download_url='http://github.com/francxk/'+component_name+'/tarball/master',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      package_data={'': ['LICENSE', 'NOTICE'],},
      install_requires=open('%s/requirements.txt' % PROJECT_ROOT).read(),
      dependency_links=open('%s/dependency_links.txt' % PROJECT_ROOT).read(),
      long_description=open('%s/README.rst' % PROJECT_ROOT).read(),
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
      license=open('%s/LICENSE.txt' % PROJECT_ROOT).read(),
      zip_safe=False,
      )