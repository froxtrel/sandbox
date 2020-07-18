# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sandbox/__init__.py
from sandbox import __version__ as version

setup(
	name='sandbox',
	version=version,
	description='for testing',
	author='e',
	author_email='me,@mail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
