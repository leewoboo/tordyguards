
* add tests!
* add man
* add doc dir (where should be placed sphinx dirs and how to install them in /usr/share/doc?)
* add repo with debian source
* reorganize code:
 * create tordyguards python package with tor_change_state.py (to be placed in /usr/lib/python2.7/dist-packages/tordyguards)
 * wicd_tor_change_state.py 
 * settings.py 
  * rename it
  * reformat it to be parsed with python configparser?
  * should it be placed in /etc/tordyguards?
  * wicd scripts path should be imported from python-wicd package (/usr/lib/python2.7/dist-packages/wicd/wpath.py)?
  * how to import tor state path from tor package?
* add gnome network manager support
* add ifupdown support