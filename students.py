from base_file import BaseClass
class Student(BaseClass):
    def __init__(self, sid, sname, sage, smarks):
        self.StudID = sid
        self.StudName = sname
        self.StudAge = sage
        self.StudMar = smarks
        self.StudSubjects = []


