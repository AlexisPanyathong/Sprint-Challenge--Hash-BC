#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # For loop: for i in range of 0 and the length of the weights.
    for i in range(0, len(weights)):
        
        # Set wt to weights[i]
        wt = weights[i]
        
        # Set retrieve to a hash table that passes in the ht and limit of the weights
        retrieve = hash_table_retrieve(ht, limit-wt)
        
        if retrieve is not None:
            first = max(i, retrieve)
            second = min(i, retrieve)
            return (first, second)
        
        hash_table_retrieve(ht, wt, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
