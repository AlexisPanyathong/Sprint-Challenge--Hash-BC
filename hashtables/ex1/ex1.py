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
        
        # set retrieve to hash table retrieve `limit - weight`
        retrieve = hash_table_retrieve(ht, limit - wt)
        
        if retrieve is None:
            # then return hash table insert
            hash_table_insert(ht, wt, i)
            
            print(f'Weight Index: {i} Value: {wt}')
        # Otherwise
        else:
            # return i, and retrieve
            return (i, retrieve)
        

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# test
test_weights = [2, 4, 6, 8]
print(get_indices_of_item_weights(test_weights, 5, 21))