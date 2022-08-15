class Person:
  def __init__(self, name, gender, maritalStatus):
    self.name = name
    self.gender = gender,
    self.maritalStatus = maritalStatus

  def getName(self):
    return self.name
  
class Student(Person):
  def __init__(self,name,gender,maritalStatus,year):
    Person.__init__(self,name,gender,maritalStatus)
    self.year = year
  def getYear(self):
    return self.year

adam = Student('ada','male','single',2)

class studentList:
  def __init__(self, persons, prop, criteria):
    self.personsList = persons
    self.prop = prop
    self.criteria = criteria
    self.peopleInCriteria = []
    self.meetsCriteria()

  def meetsCriteria(self):
    for i in self.personsList:
      if i[self.prop] == self.criteria:
        self.peopleInCriteria.append(i)

    