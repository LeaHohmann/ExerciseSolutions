class Person(object):

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def getname(self):
        print(self.firstname, self.lastname)


class Student(Person):

    def __init__(self,firstname,lastname,subject):
        Person.__init__(self,firstname,lastname)
        self.subject = subject

    def getstudentinfo(self):
        print(self.firstname, self.lastname,",", self.subject)


class Teacher(Person):

    def __init__(self,firstname,lastname,course):
        Person.__init__(self,firstname,lastname)
        self.course = course

    def getteacherinfo(self):
        print(self.firstname, self.lastname,",", self.course)
