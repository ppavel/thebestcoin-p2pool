from p2pool.bitcoin import networks

# Description of parameters could be found here: https://bitcointalk.org/index.php?topic=457574.0

PARENT=networks.nets['thebestcoin_testnet']
SHARE_PERIOD=20 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=100 # shares
SPREAD=12 # blocks
IDENTIFIER='578C5DE8CD757AC2'.decode('hex')
PREFIX='350F71041CEE442E'.decode('hex')
P2P_PORT=38803
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=38804
BOOTSTRAP_ADDRS=''.split(' ')
ANNOUNCE_CHANNEL='#p2pool-thebestcoin-testnet'
VERSION_CHECK=lambda v: True
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16
