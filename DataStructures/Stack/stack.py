from DataStructures.List import array_list as sl

def new_stack():
    my_stack = sl.new_list()
    return my_stack

def size(my_stack):
    return sl.size(my_stack)

def is_empty(stack):
    return sl.is_empty(stack)

def push(my_stack, element):
    sl.add_last(my_stack,element)
    return my_stack

def top(my_stack):
    return sl.last_element(my_stack)


def pop(my_stack):
    return sl.remove_last(my_stack)
