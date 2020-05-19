class HashTable:
    __instance = None

    # This method is used to make the HashTable a singleton class.
    # This way every file is accessing the same hashtable and only one may be created
    # Space-time complexity is O(1)
    @staticmethod
    def get_instance():
        if HashTable.__instance is None:
            HashTable()
        return HashTable.__instance

    # This method initialized the chaining hashtable
    # Space-time complexity is O(1)
    def __init__(self, initial_capacity=10):
        if HashTable.__instance is not None:
            raise Exception("Singleton class: only one instance may be created.")
        else:
            HashTable.__instance = self
            self.table = []
            for i in range(initial_capacity):
                self.table.append([])

    # A helper method to return the bucket based on a specific key
    # Space-time complexity is O(1)
    def __get_bucket_list(self, key):
        bucket = hash(key) % len(self.table)
        return self.table[bucket]

    # This method inserts a package into the hashtable
    # Space-time complexity is O(1)
    def insert(self, key, value):
        bucket_list = self.__get_bucket_list(key)
        bucket_list.append(list([key, value]))

    # This method returns a package based on its ID
    # Space-time complexity is O(N)
    def lookup(self, key):
        bucket_list = self.__get_bucket_list(key)

        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value

        print("key not found")
        return None

    # This method returns all packages stored in the hashtable
    # Space-time complexity is O(N)
    def get_all(self):
        all_packages = []
        for bucket in self.table:
            for package in bucket:
                all_packages.append(package[1])
        return all_packages

    # This method is used to update a package already stored in the hashtable
    # Space-time complexity is O(N)
    def update(self, key, new_value):
        bucket_list = self.__get_bucket_list(key)

        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = new_value

    # This method deletes a package from the hashtable
    # Space-time complexity is O(N)
    def delete(self, key):
        bucket_list = self.__get_bucket_list(key)
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove(key_value)
