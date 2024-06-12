class Main:
    def __init__(self):
        self.table = {}

    def put(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key)         

    def key_set(self):
        return self.table.keys()           

    def main(self):
        # Initialize the dictionary with some entries
        self.put(100, "Spongebob")
        self.put(123, "Patrick")
        self.put(321, "Sandy")
        self.put(555, "Squidward")
        self.put(777, "Gary")

        # Print out the entries with their hash % 10
        for key in self.key_set():
            print(hash(key) % 10, "\t", key, "\t", self.get(key))


if __name__ == "__main__":
    Main().main()
