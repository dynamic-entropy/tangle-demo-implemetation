import hashlib
import random
import numpy as np 
import string
from time import time
from collections import OrderedDict

#represents the graph data structure
tangle_graph = {
    'genesis_branch' : [], #genesis branch 
    'genesis_trunk' : [] #genesis trunk
}

tangle_data = {}

tangle_ledger = {'iota_genesis': 100}



def hash_data(data):
    data = data.encode('utf-8')
    h = hashlib.new('sha256')
    h.update(data)
    return h.hexdigest()


class transaction_block:
    def __init__(self, branch, trunk):
        self.id = ''
        self.branch = branch
        self.trunk = trunk
        self.timestamp = time.time()
        self.amount = None

    def get_hash(self):
        hash_data(OrderedDict(self.__dict__))


def add_tx(block: transaction_block):
    if block.branch in tangle_graph and block.trunk in tangle_graph:
        pass
