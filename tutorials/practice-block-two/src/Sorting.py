from functools import cmp_to_key
import inspect 
from datetime import datetime

class Name:
    first_name: str
    last_name:  str
    dob:        datetime

    def __init__(self, first_name: str, last_name: str, dob: datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def firstname(self) -> str:
        return self.first_name

    def lastname(self) -> str:
        return self.last_name
    
    def fullname(self) -> str:
        return self.first_name + " " + self.last_name

    def date_of_birth(self) -> datetime:
        return self.dob
    
    def __eq__(self, other: 'Name') -> bool:
        return self.first_name == other.first_name and self.last_name == other.last_name

    def __le__(self, other: 'Name') -> bool:
        return self.last_name <= other.last_name
        
    def __lt__(self, other: 'Name') -> bool:
        return self.last_name < other.last_name

    def __str__(self) -> str:
        return self.fullname()

    def __repr__(self) -> str:
        return self.__str__()

def bubble_sort(inlist: list, comp=None) -> list:
    n = len(inlist)
    swapped = False
    # Traverse the list
    for i in range(n-1):
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
           
def sort_builtin(people: list) -> list:
    return bubble_sort(people)

def sort_fullname(people: list) -> list:
    return bubble_sort(people, comp=Name.fullname)

def sort_dob(people: list) -> list:
    return bubble_sort(people, comp=Name.date_of_birth)

def o_pred(n1: Name, n2: Name) -> int:
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

def o_pred_new() -> int:
    return char_pred('o')

def sort_opred(people: list) -> list:
    return bubble_sort(people, comp=o_pred_new())

def char_pred(c: str):
    def res (n1: Name, n2: Name) -> int:
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
    return bubble_sort(people, comp=char_pred(c))

