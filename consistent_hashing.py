import bisect
import math

class ConsistentHashMap:
    def __init__(self, num_slots):
        self.num_slots = num_slots
        self.circle = {}  # {hash_value: server_id}
        self.sorted_keys = []

    def add_server(self, server_id):
        for i in range(9):  # Number of virtual servers
            virtual_server_id = f"{server_id}-{i}"
            hash_value = self.hash(virtual_server_id)
            self.circle[hash_value] = server_id
            self.sorted_keys.append(hash_value)
        self.sorted_keys.sort()

    def remove_server(self, server_id):
        for i in range(9):  # Number of virtual servers
            virtual_server_id = f"{server_id}-{i}"
            hash_value = self.hash(virtual_server_id)
            del self.circle[hash_value]
            self.sorted_keys.remove(hash_value)

    def get_server(self, key):
        hash_value = self.hash(key)
        idx = bisect.bisect_left(self.sorted_keys, hash_value)
        if idx == len(self.sorted_keys):
            return self.circle[self.sorted_keys[0]]
        return self.circle[self.sorted_keys[idx]]

    def hash(self, key):
        return (hash(key) + 2 * hash(key) + 17 * math.log(2)) % self.num_slots
        
