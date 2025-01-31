class Node: # defining node class, the chain of nodes will form the table
    def __init__(node, key, value): # adding __init__ function for automatic execution
        node.key = key  # Store the key
        node.value = value  # Store the value
        node.next = None  # Pointer to the next node in the chain

class HashTable:
    def __init__(table, size=10): # adding __init__ function for automatic execution
        table.size = size  # Define the size of the hash table
        table.table = [None] * table.size  # Initialize the table with empty buckets

    def _hash_function(table, key):
        return hash(key) % table.size ## Using a poor hash function to force collisions easily and test the collition handling

    def insert(table, key, value):
        index = table._hash_function(key)  # Get the hash index
        new_node = Node(key, value)  # Create a new node to be used for inserting / updating

        if table.table[index] is None:
            # If no collision, insert the new node in the given position
            table.table[index] = new_node
        else:
            # Collision handling: Add to the linked list
            current = table.table[index]
            while current:
                if current.key == key:
                    # Update value if key already exists
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node  # Insert at the end of the chain

    def search(table, key):
        index = table._hash_function(key)
        current = table.table[index]
        
        while current:
            if current.key == key:
                return current.value  # Return the value if key is found
            current = current.next
        
        return None  # Return None if key is not found

    def delete(table, key):
        index = table._hash_function(key)
        current = table.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev is None:
                    # Remove first node in chain
                    table.table[index] = current.next
                else:
                    # Bypass the node to remove it
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        
        return False  # Return False if key is not found

    def show_table(table):
        """Display the entire hash table."""
        for i, node in enumerate(table.table):
            print(f"Index {i}: ", end="")
            current = node
            while current:
                print(f"({current.key}: {current.value}) -> ", end="")
                current = current.next
            print("None")


hash_table = HashTable()
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)
hash_table.insert("apple", 15)  # Updating value

print("#### This is the table after initial insertions ####")
hash_table.show_table()

print("\n\nValue for 'banana':", hash_table.search("banana"))

hash_table.delete("orange")

print("\n\n#### This is the table after we delete orange from the table ####")
hash_table.show_table()
