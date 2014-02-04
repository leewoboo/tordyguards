#!/usr/bin/python

"""
    Wicd preconnect script that calls tor_change_state.py
    Receives the bssid Wicd is going to connect to, and call the script that
    will change the Tor state file depending on the that bssid.
    This scripts needs to be run as root,
    but wicd preconnect scripts are run by root.
"""

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


def main():

    import argparse
    try:
        from tor_change_state import change_state_file
    except ImportError:
        print 'ERROR: tor_change_state not found'

    parser = argparse.ArgumentParser(
        description='This script calls'
        ' tor_change_state.py before Wicd connects to a network to'
        ' use the tor state file associated to that network.')
    parser.add_argument('connection_type', help='(wireless, ethernet)')
    parser.add_argument('essid')
    parser.add_argument('bssid')
    args = parser.parse_args()

    change_state_file(args.bssid)

if __name__ == "__main__":
    main()
