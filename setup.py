# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in subk_addons/__init__.py
from subk_addons import __version__ as version

setup(
	name='subk_addons',
	version=version,
	description='addons and customizations for subk',
	author='Ebkar',
	author_email='admin@ebkar.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
