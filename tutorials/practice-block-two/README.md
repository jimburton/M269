# M269 Tutorial: Practice Block Two

*Dr James Burton, January 2024*

These exercises build on the code and exercises in the M269 book. We
are looking ahead to the topic of *sorting*, a major subject in data
structures and algorithms. The subject is introduced in Chapter 14,
where a variety of algorithms for sorting data are
explained. Although you won't have seen this material yet
unless you are ahead of the current week in the book, this tutorial
should be self-contained and will be useful preparation for later
on. In addition, it teaches some Python techniques that you may not
have come across yet. 

There is more work here than we can probably do in one session and the
later exercises are pretty challenging. Don't worry if you don't
finish the work during the tutorial.

*Bubble Sort* is a simple sorting algorithm. Its purpose is to
transform a collection (such as a list or an array) so that every
element is less than or equal to the subsequent element. Sorted data
can be searched in extremely efficient ways, which is why sorting is
such an important topic. Bubble Sort is far from being the most
efficient sorting algorithm but is probably the easiest to
implement. It is often used in a subsidiary role by more sophisticated
sorting algorithms that you will learn about later on this
module. I'll explain the algorithm and provide pseudocode for you
below.

Get a copy of the code by downloading a zip file from the [home
page](/) of this repository, clicking on the green **code** button. If
you are a git user, cloning the repository is the way to go. This
tutorial can be found within the repository at
[/tutorials/practice-block-two](/tutorials/practice-block-two). You
can see my version of the solutions to the exercises by switching to
the `solutions` branch of this repository. To do this on the GitHub
website, click on the button labelled **main** in the upper left hand
side of any page and select **solutions**. 

The data we will be sorting is made up of `Person`
objects. `Person` is a simple class encapsulating two strings (first
and last name) and the date of birth of a person. Read the code
here: [src/Person.py](./src/Person.py), and don't worry if there are
parts of it you don't understand right now

Before we can sort these objects we need to establish how we can
determine that one is less than, equal to or greater than another.

## Python's magic methods

Python's so-called magic methods are used to determine the default
behaviour of objects in a wide variety of ways. You've already
encountered at least one of these: the constructor method, `__init__`,
that determines what happens when we make a new instance of a
class. The names of all magic methods begin and end like `__init__`
with two underscores. Three magic methods are already defined in the
`Person` class: `__init__`, `__str__` and `__repr__`. The latter
methods allow us to govern what happens when we call `str` or `print`
on a `Person` object.

We need to define those magic methods that allow us to *order*
instances of the same class. These are `__lt__` ("less than"),
`__le__` ("less than or equal to"), `__eq__` ("equal to") and `__gt__`
("greater than").

1. Add the four comparison methods above to the [Person
   class](./src/Person.py). Each of them should take two arguments:
   `self` (like all instance methods of a class) and the object that
   we want to compare `self` to. One convention is to call the second
   argument `other`. So, the signature for `__eq__` could be:
   
   ```python
   def __eq__(self, other):
   ```
   
   Although they aren't required, you can enrich your Python code by
   adding [type
   hints](https://docs.python.org/3/library/typing.html). If you use
   them, you'll want to give the type of `other` as `Person`. However,
   Python doesn't know that this type exists until after the
   definition of the class is complete, so the way to do it is to give
   the name as a string:
   
   ```python
   def __eq__(self, other: 'Person') -> bool:
   ```
   
   For the `__eq__` method, two `Person` objects are considered equal if
   their first *and* last names are equal. For the `__lt__`, `__le__`
   and `__gt__` methods the comparison should be based on the *last
   name only*. 

2. Implement the *Bubble Sort* algorithm in the file
   [](src/Sorting.py). Do so by adding to the function that has this
   signature:
   
   ```python
   def bubble_sort(inlist: list) -> list:
   ```
   
   Suppose we have an unsorted collection, `C`, where `n` is the
   number of elements in `C`. Bubble Sort begins by comparing the
   first element of `C`, `a`, to the second, `b`. If `a` is greater
   than `b`, we swap their values. Then we compare the second element,
   `b`, to the third element, `c`. Again, if `b` is greater than `c`,
   we swap. We carry on in this way to the end of the collection, and
   call this the "first pass". By the end of the first pass the
   greatest element in the collection will have "bubbled up" all the
   way to the last position so we don't need to check it again. So on
   the first pass we loop from 0 to `n-1`. On the second pass we start
   again at the beginning and loop from 0 to `n-2`, and so on. Here is
   the pseudocode:
   
   ```
   procedure bubbleSort(A : list of sortable items)
	   n := length(A)
	   for i := 0 to n-1
	       for j := 0 to n-i-1
               # if this pair is out of order 
               if A[j] > A[j+1] then
                   # swap the values
                   swap(A[j], A[j+1]) # you need to decide how to do this
               end if
		   end for
	   end for
   end procedure
   ```

   Read this pseudocode carefully and make sure you understand
   it. Hopefully, it should be pretty easy for you to convert it to
   Python. Note that there is no `swap` function in Python and you
   should perform that step "manually", swapping the values
   yourself. 
   
   However, base your implementation on the version below, which adds
   a simple optimisation that improves performance in the best case
   scenario. That scenario occurs when the data is either already
   sorted or becomes sorted after only a few passes. If on any given
   pass we don't swap any values, then we know the data is sorted and
   we can stop. So we add a boolean flag called `swapped` to keep
   track of whether anything was swapped on the current pass. If
   nothing was swapped, we can exit the outer loop.

   ```
   procedure bubbleSort(A : list of sortable items)
	   n := length(A)
	   for i := 0 to n-1
		   swapped := false
	       for j := 0 to n-i-1
               # if this pair is out of order 
               if A[j] > A[j+1] then
                   # swap the values
                   swap(A[j], A[j+1]) # you need to decide how to do this
			       swapped := true
               end if
		   end for
		   if swapped = false:
		       break
		end for
		return A
	end procedure
   ```
   
3. Run the first unit test. It should pass if your implementation of
   Bubble Sort is correct. The unit tests are defined in the file
   [src/test_Sorting.py](./src/test_Sorting.py). IDEs like VSCode,
   PyCharm and others provide good tooling for unit tests -- easy ways
   to run them from within the editor. How you do that will depend on
   the IDE. Ask for advice in the tutorial if necessary. You can
   always run them from a terminal though. First, navigate to the
   `src/` directory. On my system, the command to run python is
   `python3` -- it may differ on yours. These are the commands to run
   all of the tests at once or just the first one:
   
   ```
   $ python3 -m unittest -v test_Sorting.Testing # runs all of the tests
   $ python3 -m unittest -v test_Sorting.Testing.test_sort_basic # runs one of the tests
   ```

The built in Python sorting methods, e.g. `sorted(list)` and
`list.sort()`, take an *optional* argument called `key` that determines
how the comparison between two objects should be made. So if we want
to sort `Person` objects by the `dob` field, instead of just using the
default way we defined in the magic methods, we could do it like this:

```python
# people is a list of Person objects
# we sort it using the built in function 'sorted'
sorted_by_dob = sorted(people, key=Person.date_of_birth)
```

We will add this feature to our own sorting function. Optional arguments
in Python are also called *keyword arguments* and are supplied with a
default value. 

4.  Change the signature of `bubble_sort` like so:

	```python
	def bubble_sort(inlist: list, key=None) -> list:
	```
	
	This adds a keyword argument called `key` with a default value of
    `None`. Users will still be able to call `bubble_sort` with just
    one argument (the list to be sorted) but they can also supply a
    second argument specifying a function to alter the way the sorting
    is done.
	
	Change the inner loop of `bubble_sort` to take account of the
    keyword argument. If its value is `None`, do the comparison
    between `Person` objects as before. If `key` was supplied, we can
    make use of it. Say the function passed in as the key was
    `Person.date_of_birth` and we want to use it to compare two
    `Person` objects, `n1` and `n2`. There are two ways to call an
    instance method (ie one that takes `self` as its first argument)
    on `n1` -- the usual way, which would be `n1.fullname()`, or we
    can write `Person.fullname(n1)`, passing in the object instance
    (`self`, which in this case is `n1`) explicitly. Since the method
    we need is bound to `key` we can write something like
	
	```python
	k1 = key(n1)
	k2 = key(n2)
	```

	where `n1` and `n2` the are elements of the list we want to
    compare. Then we make the comparison between `k1` and `k2`, the
    return values of the method calls. 
	
	We are making use here of Python's support for *first class
    functions*, a powerful feature that allows us to treat functions
    like any other value. After making these changes the tests
    `test_sort_fullname` and `test_sort_dob` should pass.

5.  Another common way to customise sorting functions is by supplying
    a *comparator function*. This is a function that takes two
    objects, e.g. two instances of `Person` and orders
    them. Typically, it does that by returning -1 if the first is less
    than the second, 0 if they are equal or 1 if the first is greater
    than the second.
	
	Say we want to sort a list of `Person` objects so that those with
    the letter "o" in their full name appear at the front of the
    list. If two `Person` objects both have an "o" in the full name,
    the one with the "o" closest to the beginning of the name should
    come first. Complete the function `o_pred` in
    [src/Sorting.py](./src/Sorting.py) so that it does this. When you
    have that working, the test `test_sort_o_pred` should pass.
	
	(NB: in the function `sort_o_pred` which is written for you, we
    need to convert `o_pred` from a comparator function to a simple
    selector method like the ones we've used so far,
    e.g. `Person.fullname`. This is the reason for the use of the
    `cmp_to_key` function.)
	
6.  Rather than hardcoding the character we want to order by, we want
    the flexibility to order by any character. Complete the function
    `char_pred` to enable that. This function should itself return a
    function (another use of first class functions). You can define
    functions *inside* functions in Python, and return them like any
    other value. The inner function should work like `o_pred` except
    that it orders `Person` objects by `c`, the argument supplied to
    the outer function `char_pred`. When you have this working the
    test `test_sort_char_pred` should pass.
	
7.  There is a lot of repetition between `o_pred` and
    `char_pred`. Change the definition of `o_pred` so that it just
    returns a call to `char_pred`. When you have done this you will
    also need to change the function `sort_o_pred`. It currently gives
    the *name* of the function object `o_pred` and looks like this:
	
	```python
	return bubble_sort(people, key=cmp_to_key(o_pred))
	```
	
	Now we need to actually *invoke* `o_pred` so that it returns the
    appropriate function object, so change it to this:
	
	```python
	return bubble_sort(people, key=cmp_to_key(o_pred()))
	```
	
8.  So far we have needed to convert comparator functions like
    `o_pred` to selector methods before passing them to the search
    routine. As mentioned above, this was done for you in functions
    called by the tests, `sort_o_pred` and `sort_char_pred`, and was
    done using the built in function `cmp_to_key`. This is also the
    way the built in Python sorting functions work -- if we want to
    pass a comparator function we have to use `cmp_to_key`. Let's make
    ours more flexible, so that we can pass in either a selector
    method or a comparator. To work out which one we're dealing with
    we will use Python's capacity for *reflection* -- this is the
    feature of being able to interrogate objects at runtime in various
    ways to find out what type of thing they are, what methods they
    have and even to alter objects by adding data and behaviour. We
    will make use of a function called `signature` from the
    [inspect](https://docs.python.org/3/library/inspect.html) module
    to tell us about the signatures of the functions passed to the
    search function.
	
	One difference between a function like `Person.fullname` and the
    inner function returned by `char_pred` is in their *arity*, which
    means the number of arguments they take. The arity of
    `Person.fullname` is 1, because like all instance methods it takes
    the argument `self`. The arity of a comparator function is 2,
    because it takes two objects to be compared.
	
	Alter the `bubble_sort` function so that when `key` is not `None`
    it first checks the arity of `key` like so:
	
	```python
	arity = len(inspect.signature(key).parameters)
	```
	
	If `arity` is 1, proceed as before. If it is 2 then we need to
    call `key` by passing in its two arguments, the objects to be
    compared. Recall that the result of this function will be an int
    which is either -1, 0 or 1.
	
	Remove the calls to `cmp_to_key` from `sort_o_pred` and
    `sort_char_pred` and see whether the tests still pass.

## Discussion

. What is the complexity of Bubble Sort?
   
