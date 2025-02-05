from functools import cmp_to_key
import inspect 
from Person import Person

# Note that rather than making incremental changes to one function
# called bubble_sort I have provided three version:
# . one that has no keyword argument, bubble_sort_no_key, matching what
#   you're asked to do for exercises 1 to 3,
# . one that takes a keyword arg and presumes it is a simple selector
#   method, bubble_sort_with_key, matching what you're asked to do
#   for exercises 4 to 7, and
# . one that takes a keyword argument but can accept a selector or
#   comparator function, bubble_sort_all_features, that matches what
#   you are asked to do for exercise 8.

def bubble_sort(inlist: list) -> list:
    """ Sort the input list using the Bubble Sort algorithm."""
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
    """ Sort the input list using the Bubble Sort algorithm. If the
        key is supplied, use that for the comparison.
    """
    n = len(inlist)
    # Traverse the list
    for i in range(0, n-1):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if key is None:
                if inlist[j] > inlist[j+1]:
                    inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                    swapped = True
            else:
                k1 = key(inlist[j])
                k2 = key(inlist[j+1])
                if k1 > k2:
                    inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                    swapped = True
        if not swapped:
            # if we haven't needed to make a single swap, we can end.
            break
    return inlist

def bubble_sort_all_features(inlist: list, key=None) -> list:
    """ Sort the input list using the Bubble Sort algorithm. If the
        key is supplied, use that for the comparison. The key may be
        a selector method or a comparator function.
    """
    n = len(inlist)
    # Traverse the list
    for i in range(0, n-1):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if key is None:
                if inlist[j] > inlist[j+1]:
                    inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                    swapped = True
            else:
                arity = len(inspect.signature(key).parameters)
                if arity == 1: # it's a method call
                    k1 = key(inlist[j])
                    k2 = key(inlist[j+1])
                    if k1 > k2:
                        inlist[j], inlist[j+1] = inlist[j+1], inlist[j]
                        swapped = True
                elif arity == 2: # it's a comparator function
                    if key(inlist[j], inlist[j+1]) > 0:
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
    return bubble_sort_with_key(people, key=Person.fullname)

def sort_dob(people: list) -> list:
    return bubble_sort_with_key(people, key=Person.date_of_birth)

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
    return bubble_sort_with_key(people, key=cmp_to_key(o_pred))

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
    return bubble_sort_all_features(people, key=char_pred(c))
