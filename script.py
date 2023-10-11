class HashMap:
    # Contructor
    def __init__(self, size):
        self.array_size = size
        self.array = [None for i in range(size)]

    # Hash method
    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    # Compression method
    def compressor(self, hash_code):
        return hash_code % self.array_size
