import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self._index = index
        self._timestamp = timestamp
        self._data = data
        self._previous_hash = previous_hash
        self._hash = self.hash_block()

    @property
    def hash(self):
        return self._hash

    @property
    def index(self):
        return self._index

    @property
    def data(self):
        return self._data

    def hash_block(self):
        sha = hasher.sha256()
        temp = str(self._index) + str(self._timestamp) + str(self._data) + str(self._previous_hash)
        sha.update(temp.encode("utf8"))
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), "种子区块", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "我是新区块 " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


block_chain = [create_genesis_block()]
previous_block = block_chain[0]
num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    block_chain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} 已经加入区块链!".format(block_to_add.index))
    print("Hash: {}".format(block_to_add.hash))
    print("Data: {}\n".format(block_to_add.data))