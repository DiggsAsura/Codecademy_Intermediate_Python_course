# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 12. Review

# Congratulations! You've completed the object-oriented programming with Python lesson. Let's
# do a quick recap of what you learned.
#
# We discussed the four pillars of object-oriented programming as they apply to the Python
# programming language.
#
# - Inheritance
#   Python allows classes to inherit on multiple levels. Meaning a class can inherit from a 
#   base class as well as a derived class. Python also supports multiple inheritance, where
#   one class can inherit from any number of other classes. This allows us to describe complex
#   relationships between objects with minimal repeated code.
#
# - Polymorphism
#   Polymorphism is a concept that allows functions and objects to behave in different ways depending
#   on context. There is the polymorphism of functions like len() or the addition operator +, 
#   which can act differently depending on the provided data.
#
# - Abstraction
#   Python supports the concept of abstraction by allowing objects with methods that have the same 
#   name, to be called in a general manner. Further, Python provides the Abstract Base Class (ABC)
#   for us to create a more clearly defined interface.
#
# - Encapsulation
#   Python's approach to encapsulation is unique compared to most other object-oriented programming
#   languages. In Python, all members of an object are publicly accessible but there are conventions
#   to indicate to developers that a member is inteneded to be protected or private.
#
# In this lesson, we learned more complicated relationships between classes. 
# We learned:
#
# - How to create a subclass of an existing class
# - How to redifine existing methods of a parent class in a subclass by overriding them
# - How to leverage a parent class's methods in the body of a subclass method using the super() function
# - How to write programs that are flexible using interfaces and polymorphism
# - How to write data types that look and feel like native data types with dunder methods
#
# These are really complicated concepts! It's a long journey to get to the state of comfortably
# being able to build class hierarchies that embody the concerns that your software will need to. 
# Give yourself a pat on the back, you earned it!

from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

class User:
  def __init__(self):
    self._username = None
  
  @property
  def username(self):
    return self._username
  
  @username.setter
  def username(self, new_name):
    self._username = new_name

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("{} added.".format(employee.username))
    self.attendees.append(employee.username)
  
  def __len__(self):
    return len(self.attendees)

class Employee(AbstractEmployee, User):
  def __init__(self, username):
    super().__init__()
    User.__init__(self)
    self.username = username
  
  def say_id(self):
    print("My id is {}".format(self.id))

  def say_username(self):
    print("My username is {}".format(self.username))
  

e1 = Employee("diggs")

print(e1.username)


# Holy hell this is overwhelming. I mean, some make sense, but some does not. 
# Brain wrinkles.