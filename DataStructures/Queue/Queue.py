from DataStructures.List import array_list as a
def new_queue():
    my_queue = a.new_list()
    return my_queue

def enqueue(my_queue, element):
    a.add_last(my_queue, element)
    return my_queue

def dequeue(my_queue):
    element = a.remove_first(my_queue)
    return element

def peek(my_queue):
    if my_queue["size"] == 0 :
        raise Exception('EmptyStructureError: queue is empty')
    
    element = a.first_element(my_queue)
    return element


def is_empty(my_queue):
    return my_queue["size"] == 0

def size(my_queue):
    return my_queue["size"]

    






   
   
