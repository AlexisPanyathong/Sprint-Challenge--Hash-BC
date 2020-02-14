#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # For loop: for i in tickets, insert the hashtable, source and the destination
    for i in tickets:
        print(i.source)
        print(i.destination)
        hash_table_insert(hashtable, i.source, i.destination)
        
    # Set the count to 0.
    count = 0
    
    # First is set to retrieve the hashtable and None
    first = hash_table_retrieve(hashtable, "None")
    route[count] = first
    current = first
    
    while current is not 'None':
        count += 1
        current = hash_table_retrieve(hashtable, current)
        route[count] = current
        
    return route
