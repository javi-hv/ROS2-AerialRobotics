
class Person:
    """
    A class to represent a person.

    Attributes
    ----------
    name : str
        The name of the person.
    age : int
        The age of the person.

    Methods
    -------
    greet():
        Prints a greeting message with the person's name.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

###########################################################################

person1 = Person("Javier", 24)
person2 = Person("Luis", 25)

person1.greet()
person2.greet()





