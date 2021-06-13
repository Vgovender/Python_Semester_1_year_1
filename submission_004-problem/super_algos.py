def find_min(element):

    if len(element) == 0 or (isinstance(element[0],int) == False):
        return -1
    elif len(element) == 1:
        return element[0]
    if element[1] < element[0]:
        element.remove(element[0])
    else:
        element.remove(element[1])
    return find_min(element)

def sum_all(element):
    if len(element) == 0 or (isinstance(element[0],int) == False):
        return -1
    if len(element) == 1:
        return(element[0])
    elif (isinstance(element[1],int) == False):
        return (-1)
    element[0] = element[0] + element[1]
    element.remove(element[1])

    return sum_all(element)


def find_possible_strings(character_set, n):
    str_len = len(character_set)
    return(find_possible_strings_rec(character_set,"",n,str_len,[]))

def find_possible_strings_rec(character_set,prefix,n,str_len,list_result):
    if n == 0:
        list_result.append(prefix)
        return []
    for i in range(str_len):
        if isinstance(character_set[i], str) == False:
            return []
        new_prefix = prefix + character_set[i]
        find_possible_strings_rec(character_set,new_prefix,n-1,str_len,list_result)
    return(list_result)


def run_program():
    my_list = [6,10,5,8]
    find_min(my_list)
    sum_all(my_list)
    set_alpha = {'x', 'y'}
    k = 3
    find_possible_strings(set_alpha,k)

if __name__ == "__main__":
    run_program()
