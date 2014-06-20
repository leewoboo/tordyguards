#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   This file is part of TorDyGuards, a set of scripts to
#   use different tor guards depending on the network we connect to.
#
#   Copyright (C) 2014 Lee Woboo (leewoboo at riseup dot net)
#   Copyright (C) 2014 Isis Lovecruft <isis@torproject.org>
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

"""Wicd preconnect script.

This script calls :func:`tordyguards.tor_change_state.change_state_file` before
Wicd connects to a network, in order to rotate Tor's ``state file``, such that
state files used by Tor are always specific to the BSSID of LAN/WLAN network
access point that Wicd is about to attempt to connect to.

What does this thing do?
~~~~~~~~~~~~~~~~~~~~~~~~
The primary purpose for this is to force Tor to use different ``EntryGuards``
(hereafter, simply called "Guards" in this documentation) per network.

Okay. But why would I want to use this thing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Without using this script to rotate Tor's state files, Tor will, by default,
use the same set of Guards as entry points into the Tor network for several
months at a time. At the time of writing, Tor's current default settings
vis-á-vis Guards are to use three Guards (i.e. the ``NumEntryGuards``
setting), and to only make outgoing connections through those three Guards,
for as long as the Tor ``DirectoryAuthority``s recommend to do so in their
``GuardLifetime`` parameter (the ``DirectoryAuthority``s specify this setting
to Tor clients in the Tor consensus, which is a list of all the agreed-upon
relays in the Tor network).

Assuming an adversary has visibility into your local network connection
attempts, using three Guards is a fingerprinting mechanism, which may be used
by an adversary to track your physical location, particularly if you are using
Tor from a mobile device. 

.. note:: This **does not** imply that such an adversary should necessarily
    have any greater advantage in deanonymising your traffic sent through Tor,
    e.g. knowing which websites you're visiting.

However, it is **does** mean that such an adversary would be able to watch you
connect to your three Guards at your house in the morning, then later at your
favourite coffee shop, and again, later, at your office or
school. Statistically, with 1200 relays capable of being used as Guards in the
Tor network, the probability that your choice of Guards would be the same as
someone else's is given by a very simple, rough estimate:

      ⎛ ₙ    ⎞ ₙ
     P⎜⋂   Aᵢ⎟ ∏ P(Aᵢ)  where P(A)=1/1200 and n=3
      ⎝ ⁱ⁼¹  ⎠ⁱ⁼¹
so
     P(A₁) P(A₂) P(A₃) = (1/1200)³ ~= 1/1,700,000,000

This ignores that each individual Guard is assigned a weighted probability
based on its measured network bandwith capacity. However, even if your three
Guards are the highest capacity Guards (meaning that you're in the largest
anonymity set, and the above 1:1.7e9 probability for colision with other users
of the same set of Guards is much lower), the numbers should still surpass the
estimates on daily number of Tor users worldwide. Thus, Guard selection
provides local adversaries with an excellent fingerprinting mechanism for
tracking a user's physical location.

That was to mathy. What does this thing do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To uncorrelate Guard selection from the individual user, that user should pick
a set of Guards specific to each network which the user connects to, and use
those Guards in the same manner as regular Tor users.

This script is meant to work with Wicd, and it should live in
``/etc/wicd/hooks/preconnect/``. It receives the BSSID Wicd is about to
attempt to connect to, and it will change the Tor state file depending on the
that BSSID. This scripts needs to be run as root, but Wicd preconnect scripts
are run by root.
"""

from __future__ import print_function

import argparse


CONFIG_FILENAME = '/etc/tordyguards/tordyguards.conf'


def main():
    try:
        import tor_change_state
    except ImportError, error:
        print(error)
        exit('ERROR: tor_change_state not found!')

    parser = argparse.ArgumentParser(description=(
        "This script is called before Wicd connects to a network, in order "
        "to rotate Tor's state file, such that state files used by Tor are "
        "always specific to the BSSID of LAN/WLAN network access point that "
        "Wicd is about to attempt to connect to."))
    parser.add_argument('-f', '--config', help='tordyguards config file',
                        default=CONFIG_FILENAME)
    parser.add_argument('connection_type', help='(wireless, ethernet)')
    parser.add_argument('essid')
    parser.add_argument('bssid')
    args = parser.parse_args()

    tor_change_state.change_state_file(args.bssid, config_file=args.config)


if __name__ == "__main__":
    main()
