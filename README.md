TorDyGuards - Tor dynamic guards
===================================

Use different [Tor](https://www.torproject.org/ "Tor") 
[entry guards](https://www.torproject.org/docs/faq#EntryGuards "entry guards") 
depending on the network we connect to.

By default, Tor store the Tor guards in the Tor state file. 
If a user is connecting to the Internet from different physical locations 
(and therefore, different networks), using the same Tor entry guards, might 
break location anonymity. To know more about this topic read [this link](
https://blog.torproject.org/category/tags/entry-guards)

How it works
-------------

TorDyGuards will create a different state file for each different network bssid
 (`state.<bssid>`) and a file with the bssid of the last network (`last_bssid`).
The bssid of the network we are connenting to is provided by a network manager.

TorDyGuards can not know when Tor is stop manually nor when we use a different
network manager, so it will assume that the state file found corresponds to the
last bssid stored, what might not be correct.

When TorDyGuards is run, it will search for a state file that match the bssid
of the network is connecting to. 
If it is found and is different to the last known bssid (in `last_bssid`), 
it moves the current state to the the last known bssid (`state.<last_bssid>`) 
and copies the matching state file (`state.<current_bssid>`) to state.
If it is found and is the same as the last known bssid, it just update the 
`state.<current_bssid`> copy.
If it is not found, but there is a last known bssid, the current state file is
moved to that bssid `state.<last_bssid>`. Tor will create a new state file.
If it is not found, and there is not any last known bssid (ie. first time this
program is run), it will move the current state to state.old and create the 
`last_bssid` file with the current bssid.

TorDyGuards could have use just replaced the state file with symoblic links to
the `state.<bssid>` files, but the Tor version used, ignored the links.


Current status
---------------

Currently, TorDyGuards only supports [Tor Debian package](
http://packages.debian.org/search?keywords=Tor "Tor Debian package") and 
[Wicd network manager](https://launchpad.net/wicd "Wicd"). 

TorDyGuards contains:
* `tor_change_state.py`, the script that reads/write the Tor state files in 
  `/var/lib/tor/`
* `settings.py`, the file where the Tor path and user are stored.
* `wicd_tor_change_state.py`, the script that, when placed in 
  `/etc/wicd/scripts/preconnect`, will receive the bssid of the network the user
  is connecting to, and call `tor_change_state.py` with it.

Adding support for other Tor packages and other network managers
-----------------------------------------------------------------

To support other Tor packages, for instance, [Tor Browser Bundle](
https://www.torproject.org/projects/torbrowser.html.en "Tor Browser Bundle"), 
the path and user that Tor uses can be changed in the settings.py file.
However it would be more convient to try to detect it or ask the user when 
installing TorDyGuards.

Other networks managers (or ways to connect to the connect) that could be 
supported:

 * no network manager: if network configurations are directly used from 
   `/etc/network/interfaces` and/or `/etc/wpa_supplicant/wpa_supplicant.conf`, 
   an script should be placed in `/etc/network/if-up.d/`.
 * Gnome Network Manager
 * add your favourite network manager here


Installation
--------------

See INSTALL.md


License
---------

Copyright (C) 2014 Lee Woboo (leewoboo at riseup dot net)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.