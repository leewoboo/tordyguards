# Constants for tor_change_state.py

# TODO: place these configurations in a more suitable location
# TODO: add support for TBB, tor path and user are different
# TODO: try to guess these values from the system
TOR_STATE_PATH = '/var/lib/tor'
TOR_STATE_FILE = 'state'
TOR_STOP_CMD = 'service tor stop'
TOR_START_CMD = 'service tor start'
TOR_USER = 'debian-tor'
# keep in a separate file which was the last network bssid
LAST_BSSID_FN = 'last_bssid'
