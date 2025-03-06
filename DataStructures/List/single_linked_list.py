from DataStructures.List import list_node as n

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"] 

def is_present(my_list, element, cmp_function):
    is_in_array= False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    node = n.new_single_node(element)
    node["next"] = my_list["first"]
    my_list["first"] = node
    
    if my_list["last"] is None:
        my_list["last"] = node
    my_list["size"] += 1
    
    return my_list


def add_last(my_list, element):
    node = n.new_single_node(element)
    if  my_list["last"] is None:
        my_list["last"] = node
        my_list["first"] = node
        my_list["size"] += 1
    else:
    
        
        temp = my_list["first"]
        while temp["next"] != None:
            temp = temp["next"]
        temp["next"] = node
        node["next"] = None
        my_list["last"] = node

        my_list["size"] += 1
    
    return my_list

def size(my_list):
    
    return my_list["size"]   

def first_element(my_list):

    return my_list["first"]["info"]


def is_empty(my_list):
    
    if my_list["size"]==0:
        empty = True
    else:
        empty = False 
    return empty


def last_element(my_list):


    return my_list["last"]["info"]


def remove_first(my_list):
    if my_list["size"] == 0:
        return None
    
    node = my_list["first"]["info"]

    my_list["first"] = my_list["first"]["next"] 

    my_list["size"] -= 1

    if my_list["size"] == 0:  
        my_list["last"] = None
        my_list["first"] = None
    
    
    return node
#final test

def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    element = my_list["last"]["info"]
   
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
    
    else:

        node = my_list["first"]
        
        while node["next"] != my_list["last"]:

            node = node["next"]
        node["next"] = None
        my_list["last"] = node
        my_list["size"] -= 1
    return element

def insert_element(my_list, element, pos):
    node = n.new_single_node(element)
    if pos < 0 or pos > size(my_list):
        print("posicion no valida")
        return my_list
    elif pos == 0:
        node["next"] = my_list["first"]
        my_list["first"] = node
        if my_list["last"] is None:
            my_list["last"] = node
        my_list["size"] += 1
        return my_list
    
    temp = my_list["first"]
    for i in range(pos - 1):
        temp = temp["next"]
    
    node["next"] = temp["next"]
    temp["next"] = node
    my_list["size"] += 1
    return my_list


def delete_element(my_list, pos):

    if pos == 0:
        my_list["first"] = my_list["first"]["next"]

    else:
        temp = my_list["first"]
        actual_pos = 0

        while actual_pos < pos-1:
            temp = temp["next"]
            actual_pos +=1
        temp["next"]= temp["next"]["next"]
        my_list["size"] -= 1

    return my_list


def change_info(my_list, pos, new_info):
    
    temp= my_list["first"]
    actual_pos = 0
    while actual_pos < pos:
        temp = temp["next"]
        actual_pos += 1
    temp["info"] = new_info
    
    return my_list

def sub_list(my_list, pos, newelem):
    sublst = new_list()
    i = 0

    while i < newelem and pos < size(my_list):
        element = get_element(my_list, pos)
        add_last(sublst, element)
        pos += 1
        i += 1

    return sublst


def exchange(my_list, pos1, pos2):
    p1= my_list["first"]
    p2 = my_list["first"]
    c1 = 0
    c2 = 0
    while c1< pos1:
        p1 = p1["next"]
        c1 +=1
    e1= p1["info"]


    while c2 < pos2:
        p2 = p2["next"]
        c2 += 1
    e2 = p1["info"]


    p1["info"] = e2
    p2["info"] = e1

    return my_list


     





