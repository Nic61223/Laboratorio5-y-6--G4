def new_list():
    newlist ={
        'elements': [],
        'size':0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0 :
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0 :
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def first_element(my_list):
    if my_list["size"] == 0:
        return None
    else:
        return my_list["elements"][0]

def last_element(my_list):
    if is_empty(my_list):
        return None
    else:
        return my_list["elements"][my_list["size"] - 1]


def size(my_list):
    return my_list["size"]
       
def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def is_empty(my_list):
    
    if my_list["size"]==0:
        empty = True
    else:
        empty = False 
    return empty
    
    
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def get_last_element(my_list):
    return my_list[-1]



def get_element(my_list, pos):
    return my_list["elements"][pos]
   #prueba final
   #  
    
def delete_element(my_list, pos):
    new_elements = []
    count = 0
    for item in my_list["elements"]:
        if count == pos:
            count = count + 1
        else:
            new_elements += [item]
            count = count + 1

    my_list["elements"] = new_elements
    my_list["size"] =   my_list["size"] - 1
    return my_list


def remove_first(my_list):
    if my_list["size"] == 0:
        return None
    else:

        element = my_list["elements"].pop(0)
        my_list["size"] = my_list["size"]-1
    
    return element


def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    else:

        element = my_list["elements"].pop(-1)
        my_list["size"] = my_list["size"]-1
    
    return element


def insert_element(my_list, element, pos):
    new_elements = []
    count = 0
    for item in my_list["elements"]:
        if count == pos:
            new_elements += [element]
        new_elements += [item]
        count = count + 1

    if pos == count:
        new_elements += [element]

    my_list["elements"] = new_elements
    my_list["size"] = my_list["size"] + 1
    return my_list



def change_info(my_list, pos, new_info):
    my_list[pos] = new_info
    return my_list


def exchange(my_list, pos_1, pos_2):
    el1 = my_list["elements"][pos_1]
    el2 = my_list["elements"][pos_2]
    my_list["elements"][pos_1] = el2
    my_list["elements"][pos_2] = el1
    return my_list

def sub_list(my_list, pos, numelem):
    i = pos
    contador = 0
    new = new_list()

    while i < len(my_list["elements"]) and contador < numelem:
        new["elements"].append(my_list["elements"][i])
        i +=1
        contador +=1
    
    new["size"] = len(new["elements"])
    return new
        


