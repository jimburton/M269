from functools import cmp_to_key
import inspect 
from Person import Person

def bubble_sort(inlist: list) -> list:
    # remove the line below when writing your code
    pass

# These functions are called by the tests

def sort_basic(people: list) -> list:
    return bubble_sort(people)

def sort_fullname(people: list) -> list:
    return bubble_sort(people, key=Person.fullname)

def sort_dob(people: list) -> list:
    return bubble_sort(people, key=Person.date_of_birth)

def o_pred(n1: Person, n2: Person) -> int:
    # remove the line below when writing your code
    pass

def sort_o_pred(people: list) -> list:
    return bubble_sort(people, key=cmp_to_key(o_pred))

def char_pred(c: str):
    # remove the line below when writing your code
    pass

def sort_char_pred(people: list, c: str) -> list:
    return bubble_sort(people, key=cmp_to_key(char_pred(c)))

