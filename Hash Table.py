class HashTable:
    collection = {}

    def __init__(self):
        pass

    def hash(self, string):
        return sum(ord(character) for character in string)

    def add(self, key, value):
        created_hash = self.hash(key)

        if created_hash not in HashTable.collection:
            HashTable.collection[created_hash] = {}

        HashTable.collection[created_hash][key] = value

        return HashTable.collection

    def remove(self, key):
        computed_hash = self.hash(key)

        if computed_hash in HashTable.collection:
            bucket = HashTable.collection[computed_hash]

            if key in bucket:
                del bucket[key]

            if not bucket:
                del HashTable.collection[computed_hash]

        return HashTable.collection

    def lookup(self, key):
        calculated_hash = self.hash(key)

        if calculated_hash in HashTable.collection:
            return HashTable.collection[calculated_hash].get(key)

        return None





