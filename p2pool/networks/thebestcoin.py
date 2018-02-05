from p2pool.bitcoin import networks

# Description of parameters could be found here: https://bitcointalk.org/index.php?topic=457574.0

PARENT=networks.nets['thebestcoin']
SHARE_PERIOD=20 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=100 # shares
SPREAD=12 # blocks
IDENTIFIER='191C76DD84EA7C08'.decode('hex')
PREFIX='23130456E2B9E62F'.decode('hex')
P2P_PORT=38801
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=38802
BOOTSTRAP_ADDRS=''.split(' ')
ANNOUNCE_CHANNEL='#p2pool-thebestcoin'
VERSION_CHECK=lambda v: True
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16
