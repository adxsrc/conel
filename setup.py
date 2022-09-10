#!/usr/bin/env python3
#
# Copyright (C) 2022 Chi-kwan Chan
# Copyright (C) 2022 Steward Observatory
#
# This file is part of conel.
#
# conel is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# conel is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with conel.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages


setup(
    name='conel',
    version='0.0.0',
    url='https://github.com/adxsrc/conel',
    author='Chi-kwan Chan',
    author_email='chanc@arizona.edu',
    description='CONnected-ELemanifold: data structures and algorithms for computational topology',
    packages=find_packages('mod'),
    package_dir={'': 'mod'},
    python_requires='>=3.7',
    install_requires=[
    ],
)
