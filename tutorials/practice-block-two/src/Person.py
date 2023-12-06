from datetime import datetime

class Person:
    """ The Person class represents a person's name and their date of birth."""
    
    first_name: str      # The first name
    last_name:  str      # The last name
    dob:        datetime # The date of birth

    def __init__(self, first_name: str, last_name: str, dob: datetime):
        """ Construct a new Person object, given the first name, last name
            and date of birth.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def firstname(self) -> str:
        """ Get the first name."""
        return self.first_name

    def lastname(self) -> str:
        """ Get the last name."""
        return self.last_name
    
    def fullname(self) -> str:
        """ Get the full name, which is the concatenation of the first
            and last names.
        """
        return self.first_name + " " + self.last_name

    def date_of_birth(self) -> datetime:
        """ Get the date of birth."""
        return self.dob

    def __str__(self) -> str:
        """ Get a string representation of this object."""
        return self.fullname()

    def __repr__(self) -> str:
        """ This method is called when objects are passed to the `str' method."""
        return self.__str__()
    
    def __eq__(self, other: 'Person') -> bool:
        """ Compare two Person objects for equality. Two Person objects are equal
            if their first and last names are equal.
        """
        return self.first_name == other.first_name and self.last_name == other.last_name

    def __le__(self, other: 'Person') -> bool:
        """ Returns true is self is less than or equal to the other. One Person
            object is less than or equal to another if its last name is (lexicographically)
            less than or equal to the last name of the other.
        """
        return self.last_name <= other.last_name
        
    def __lt__(self, other: 'Person') -> bool:
        """ Returns true is self is less than the other. One Person
            object is less than another if its last name is (lexicographically)
            less than the last name of the other.
        """
        return self.last_name < other.last_name

    def __gt__(self, other: 'Person') -> bool:
        """ Returns true is self is greater than the other. One Person
            object is greater than another if its last name is (lexicographically)
            greater than the last name of the other.
        """
        return self.last_name > other.last_name
