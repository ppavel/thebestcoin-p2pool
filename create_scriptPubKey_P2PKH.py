#!/usr/bin/env python

# usage example:
# python create_scriptPubKey_P2PKH.py 7DHFyvoe6XaCxdxkhR9eu8Qptp6oHevXJC thebestcoin
# python create_scriptPubKey_P2PKH.py bHtbYYwcypJoaNm5gdDwKaaeByfHMk92sN thebestcoin_testnet

import sys
from p2pool.bitcoin import data as bitcoin_data, networks

def main(address, network_name):
    pubkeyHash = bitcoin_data.address_to_pubkey_hash(address, networks.nets[network_name])
    P2PKH = bitcoin_data.pubkey_hash_to_script2(pubkeyHash).encode('hex')

    print "scriptPubKey P2PKH hex: " + P2PKH

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
