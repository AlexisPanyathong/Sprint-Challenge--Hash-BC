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
        
        # hash table insert function ht, source, and destination
        hash_table_insert(hashtable, i.source, i.destination)
        
    # Set the count to 0.
    # count = 0
    
    # account for NONE
    destination = hash_table_retrieve(hashtable, 'NONE')
    
    while destination is not 'None':
        # append destination to route
        route.append(destination)
        # destination set to retrieve ht, destination
        destination = hash_table_retrieve(hashtable, destination)
        
    return route
