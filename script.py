from linked_list import Node, LinkedList

class HashMap:
    # Contructor
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(size)]

    # Hash method
    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    # Compression method
    def compressor(self, hash_code):
        return hash_code % self.array_size

    # Assign new hash
    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        self.array[array_index] = [key, value]

    # Hash retrieval
    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        payload = self.array[array_index]

        if payload is None:
            return None

        if payload[0] != key:
            return None

        if payload[0] == key:
            return payload[1]
