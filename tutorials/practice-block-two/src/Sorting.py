from functools import cmp_to_key
import inspect 
from Person import Person

def bubble_sort_no_key(inlist: list, key=None) -> list:
    n = len(inlist)
    # Traverse the list
    for i in range(0, n-1):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if inlist[j] > inlist[j+1]:
                inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                swapped = True
        if not swapped:
            # if we haven't needed to make a single swap, we can end.
            break
    return inlist

def bubble_sort_with_key(inlist: list, key=None) -> list:
    n = len(inlist)
    # Traverse the list
    for i in range(0, n-1):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if key == None:
                if inlist[j] > inlist[j+1]:
                    inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                    swapped = True
            else:
                x_func = getattr(inlist[j], key.__name__)
                y_func = getattr(inlist[j+1], key.__name__)
                if x_func() > y_func():
                    inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                    swapped = True
        if not swapped:
            # if we haven't needed to make a single swap, we can end.
            break
    return inlist

def bubble_sort_all_features(inlist: list, comp=None) -> list:
    n = len(inlist)
    # Traverse the list
    for i in range(0, n-1):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if comp == None:
                if inlist[j] > inlist[j+1]:
                    inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                    swapped = True
            else:
                arity = len(inspect.signature(comp).parameters)
                if arity == 1: # it's a method call
                    x_func = getattr(inlist[j], comp.__name__)
                    y_func = getattr(inlist[j+1], comp.__name__)
                    if x_func() > y_func():
                        inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                        swapped = True
                elif arity == 2: # it's a comparator function
                    if comp(inlist[j], inlist[j+1]) > 0:
                        inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                        swapped = True
                else:
                    print("Wrong arity: "+arity)
        if not swapped:
            # if we haven't needed to make a single swap, we can end.
            break
    return inlist

def sort_basic(people: list) -> list:
    return bubble_sort_no_key(people)

def sort_fullname(people: list) -> list:
    return bubble_sort_with_key(people, comp=Person.fullname)

def sort_dob(people: list) -> list:
    return bubble_sort_with_key(people, comp=Person.date_of_birth)

def o_pred(n1: Person, n2: Person) -> int:
    if 'o' in n1.fullname() and not 'o' in n2.fullname():
        return -1
    elif 'o' in n1.fullname() and 'o' in n2.fullname():
        if n1.fullname().find('o') < n2.fullname().find('o'):
            return -1
        elif n1.fullname().find('o') == n2.fullname().find('o'):
            return 0
        else:
            return 1
    elif 'o' in n2.fullname():
        return 1
    else:
        return 0

def o_pred_using_char_pred() -> int:
    return char_pred('o')

def sort_o_pred(people: list) -> list:
    return bubble_sort_with_key(people, comp=cmp_to_key(o_pred_using_char_pred()))

def char_pred(c: str):
    def res (n1: Person, n2: Person) -> int:
        if c in n1.fullname() and not c in n2.fullname():
            return -1
        elif c in n1.fullname() and c in n2.fullname():
            if n1.fullname().find(c) < n2.fullname().find(c):
                return -1
            elif n1.fullname().find(c) == n2.fullname().find(c):
                return 0
            else:
                return 1
        elif c in n2.fullname():
            return 1
        else:
            return 0
    return res

def sort_char_pred(people: list, c: str) -> list:
    return bubble_sort_all_features(people, comp=char_pred(c))

