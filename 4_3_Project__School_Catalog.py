# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 3. Project
# School Catalogue

# Let's put your knowledge of classes to the test by creating a digital school
# catalog for the New York City Department of Education. The Department of 
# Education wants the catalog to hold quick reference material for each 
# school in the city.
#
# We need to create classes for primary and high schools. Because these classes
# share properties and methods, each will inherit from a parent School class.
# Our parent and three child classes have the following properties, getters,
# setters and methods:
#
# School
#   - Properties: name (string), level (one of three strings: 'primary', 
#     middle' or 'high'), and numberOfStudents (integer)
#
#   - Getters: all properties have getters
#
#   - Setters: all numberOfStudents property are setters
#
#   - Methods: A __reprs__ method that displays information about the school
#
# Primary
#   - Includes everything in the School class, plus one additionl property
#
#   - Properties: pickupPolicy (string, like "Pickup after 3pm")
#
# Middle
#   - Does not include any additional properties or methods
#
# High
#   - Includes everything in School class, plus one additional property
#   - Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])

class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  def get_name(self):
    return self.name

  def get_level(self):
    return self.level
  
  def get_numberOfStudents(self):
    return self.numberOfStudents
  
  def set_numberOfStudents(self, new_numberOfStudents):
    self.numberOfStudents = new_numberOfStudents
    #return new_numberOfStudents
  
  def __repr__(self):
    return "A {level} school named {name} with {n} students".format(level=self.level, name=self.name, n=self.numberOfStudents)
    

class Primary():
  pass

class Middle():
  pass

class High():
  pass


s1 = School("Raumyr", "Primary", 400)
print(s1)
#print(s1.get_name())
#print(s1.get_level())
#print(s1.get_numberOfStudents())



