class HashMap:
    # Contructor
    def __init__(self, size):
        self.array_size = size
        self.array = [None for i in range(size)]
