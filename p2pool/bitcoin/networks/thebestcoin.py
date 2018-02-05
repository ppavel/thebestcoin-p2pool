import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

# Description of parameters could be found here: https://bitcointalk.org/index.php?topic=457574.0

P2P_PREFIX='e77e26a5'.decode('hex')
P2P_PORT=8801
ADDRESS_VERSION=15
RPC_PORT=8802
RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
    'thebestcoinaddress' in (yield bitcoind.rpc_help()) and
    not (yield bitcoind.rpc_getinfo())['testnet']
))
SUBSIDY_FUNC=lambda height: 10000*100000000 >> (height + 1)//110000
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('lyra2re2_hash').getPoWHash(data))
BLOCK_PERIOD=120 # s
SYMBOL='BC'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'TheBestCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/TheBestCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.thebestcoin'), 'thebestcoin.conf')
BLOCK_EXPLORER_URL_PREFIX='http://explorer.thebestcoin.io/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://explorer.thebestcoin.io/address/'
TX_EXPLORER_URL_PREFIX='http://explorer.thebestcoin.io/tx/'
SANE_TARGET_RANGE=(2**256//1000000000000000000 - 1, 2**256//100000 - 1)
DUMB_SCRYPT_DIFF=256
DUST_THRESHOLD=0.03e8
