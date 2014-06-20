#!/usr/bin/python

#   This file is part of TorDyGuards, a set of scripts to
#   use different tor guards depending on the network we connect to.
#
#   Copyright (C) 2014 Lee Woboo (leewoboo at riseup dot net)
#
#   TorDyGuards is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License Version 3 of the
#   License, or (at your option) any later version.
#
#   TorDyGuards is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with TorDyGuards.  If not, see <http://www.gnu.org/licenses/>.
#

from distutils.core import setup, Command
from distutils.extension import Extension
import os
import sys
import shutil
import subprocess
from glob import glob

VERSION = '0.2'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

dependencies = [
    'wicd',
    'tor',
]

# argparse and ordereddict are included in Python starting in 2.7
if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    dependencies.append('argparse')

setup(
    name="tordyguards",
    version=VERSION,
    description="Wicd script to use different Tor entry guards "
    "depending on the network we connect to.",
    long_description=read('README.md'),
    author="Lee Woboo",
    author_email="leewoboo@riseup.net",
    url="https://github.com/leewoboo/tordyguards",
    license="http://www.gnu.org/licenses/old-licenses/gpl-3.0.html",
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Environment :: Console",
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    # package_dir={'tordyguards': 'src'},
    # packages=['tordyguards'],
    # scripts=['scripts/tordyguards.py'],
    data_files=[
        ('/etc/wicd/scripts/preconnect', ['bin/tordyguards.py']),
        ('/etc/wicd/scripts/preconnect', ['src/tor_change_state.py']),
        ('/etc/tordyguards', ['tordyguards.conf']),
        # ('/usr/share/man/man1', ['man/tordyguards.1']),
        # ('/usr/share/doc/tordyguards', ['doc/source/*.rst'])
    ],
    requires=dependencies,
)
