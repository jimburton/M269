# M269 Tutorial: Practice Block Two

*Dr James Burton, January 2024*

These exercises build on the code and exercises in the M269 book,
especially the material relating to *classes* and the
*object-oriented* style of programming (OOP) in Python. The purpose of
M269 is not to teach OOP of course, but classes are used throughout
the examples and so some further practice with key OOP concepts is
useful. Along with the class itself, these concepts include *objects*
(also called *instances*), *inheritance*, *overriding* and
*overloading*, , *instance variables* and *class variables*. This
short tutorial will provide experience with all of these concepts.

## Brief overview of OOP in Python

Classes provide a container in which to define certain *data* (stored
in variables) and *behaviour*, encapsulated in methods. After defining
a class we use it as a sort of template to produce objects which are
called *instances* of that class. Here's a class that represents data
and behaviour of two dimensional geometric shapes:

```python
class Shape:
		
	def area(self) -> float:
		pass
		
	def perimeter(self) -> float:
		pass
```

This class doesn't do anything useful as yet. To make a new instance
of it we use the class name as a special sort of method, e.g. `myShape
= Shape()`. Then we can call any of the methods defined on the class,
e.g. `myShape.area()` or `myShape.perimeter()`. Note that these
methods take a parameter called `self` as their first argument. This
is a Python keyword (so it has to be spelled in exactly this way) that
refers to the instance of the class on which the method was called. So
the result of calling either method on one instance might not be the
same as calling it on another. This is one of the main points of OOP:
each object can contain its own data and behaviour.

Our `Shape` class represents a very general and abstract idea of a
geometric shape. We know that every 2D shape has an area and a
perimeter, but without knowing what kind of shape it is we can't say
more than that. To make concrete use of it we can define classes that
*inherit* from `Shape` but add their own specific details about actual
shapes.

```python
class Circle(Shape):
	
	radius: int
	
	__init (self, radius: int):
		self.radius = radius
		
	def area (self) -> float:
		return math.pi * (self.radius * self.radius)
		
	def perimeter (self) -> float:
		return 2 * math.pi * self.radius
```

The first line defines our new class, `Circle`, to be a *subclass* of
`Shape`. That means that it *inherits* all the data and behaviour of
`Shape`, as well as being able to define its own. On the first line of
code within the class definition, we define a new *instance variable*,
`radius`. A radius is a property that every circle will have, but each
may differ. If there were some value that we wanted all instances of
`Circle` to share, we would store that in a *class variable* (also
called a *static* variable). Python is not a strictly object-oriented
language. So, unlike many languages, it doesn't have an inbuilt way to
deal with constant values that can't be changed. The convention is to
give such variable an upper case name and trust that everyone will
leave them alone.

The first method, `__init__`, is called the *constructor* and is the
code that gets called when we create an instance of our class: e.g. `c
= Circle(4)` creates a new circle with radius of 4. Note that we don't
supply the `self` argument ourselves -- indeed, we couldn't in this
case as the object hasn't been created yet. The Python runtime takes
care of that for us. Within the constructor we use `self` to
disambiguate `raduis` the instance variable from `radius` the
parameter of the method (if we had called one of them something else
we wouldn't have needed to do this). That is, `self.radius` always
refers to the instance variable whereas `radius` takes the closest
binding it can, which in this case is the formal parameter, which is
local to the constructor method.

Finally, note that we provided specific ways of calculating the shape
and perimeter of circles. Here's our next shape:

```python
class Square(Shape):
	
	size: int
	
	__init__ (self, size: int):
		this.size = size
		
	def area (self) -> float:
		return (self.size * self.size)
	
	def perimeter(self) -> float:
		return self.size * 4
```

Here we need different data, or instance variables, and different
implementations of the `area` and `perimeter` methods. We could go on
to define many different types of shape, and each would need to know
different things in order to calculate things like their area and
perimeter. However, they would all be instances of `Shape`. A subclass
(or *child* class) has the type of its superclass (or *parent* class)
as well as having its own type. An example of how that is useful and
helps us write neat code:

```python
c = Circle(8)
s = Square(5)
shapes = [c, s]

var areaSum = 0
for shape in shapes:
	# whatever type of shape this we know it has an area method
	areaSum = areaSum + shape.area() 
```

## Design patterns and sandwiches

Software made up of classes and objects can become very convoluted if
not designed carefully, meaning that it ends up being very hard to
maintain and extend. The same issues of design come up repeatedly, and
the solutions to these recurring problems are called *design
patterns*. Each design pattern explains the nature of the problem and
proposes a confuration of classes and objects that solves it,
sometimes also with algorithms for handling the objects. One such
example is the *Decorator* pattern.

Suppose we are writing software to be used in a sandwich shop. Our
software needs to calculate the prices of individual sandwishes and
keep track of the stock being used in the shop. 

We will start off by making a `Sandwich` superclass. All of our
sandwiches will have a price and a description.

```python
class Sandwich():

	cost: int # the cost in pennies
	description: string # the description
	
	def cost(self) -> int:
		# get the cost in pennies
		pass
		
	def describe(self) -> string:
		# get the description of the sandwich
		pass
```

We can then go on to create subclasses to represent all the different
types of sandwiches we have for sale (cheese, ham, chicken, falafels
etc etc) each using different kinds of bread (white, brown, rye,
etc). This would lead to a very messy design with, potentially,
*hundreds* of subclasses! Furthermore, each sandwich can have any
number of toppings (lettuce, mayonnaise, ketchup, gherkins etc
etc). We could choose to represent these as boolean instance
variables, setting them to `true` if the customer wants that topping,
otherwise `false`. This would lead to more messy code and whenever we
want to add a new topping we have to make changes in many places.

This is the kind of problem that *Decorator* solves. It allows us to
add data and behaviour to objects dynamically. The idea is that
we create a subclass of sandwich which "wraps" or decorates another
instance of the same class.

```python
class SandwichDecorator(Sandwich):

	sandwich: Sandwich
	
	def __init__(self, sandwich: Sandwich):
		self.sandwich = sandwich
```

Now we create a couple of subclasses that can be used as the basis of
sandwiches. These will be used to create the objects to be
decorated. We'll take the type of bread to be used as the most basic
aspect of sandwiches, and just show one variant.

```python
class RyeBreadSW(Sandwich):
	
	def cost(self) -> int:
		return 200
		
	def describe(self) -> string:
		return " on rye bread."

# similar classes are needed for the other kinds of bread we use
```

Now we create subclasses of `SandwichDecorator`, each of which adds a
single characteristic to the sandwich: the main ingredient, the type
of bread, or a topping. Here are several such classes.

```python
class CheeseSW(SandwichDecorator):

	def cost(self) -> int:
		return self.sandwich.cost + 150
		
	def describe(self) -> string:
		return "Cheese sandwich " + self.sandwich.description
		
class LettuceSW(SandwichDecorator):

	def cost(self) -> int:
		return return self.sandwich.cost + 50
		
	def describe(self) -> string:
		return "with lettuce " + self.sandwich.description
```

Here's the code to create a cheese sandwich with mayonnaise on rye
bread:

```python
>>> mySandwich = LettuceSW(CheeseSW(RyeBreadSW()))
>>> print(mySandwich.describe())
"Cheese sandwich with lettuce on rye bread"
>>> print(mySandwich.cost())
400
```
When we introduce a new topping we just need a new subclass of
`SandwichDecorator`. This solution will provide a codebase which is
much easier to maintain and add to than the other potential solutions. 

Beyond our toy example, *Decorator* has many uses. It is often used in
GUI frameworks to allow widgets to be composed, or nested within each
other, in such a way that parent widgets ask their children to draw
themselves, before the parent is drawn.
