from base_file import BaseClass
class Department(BaseClass):
    def __init__(self, cid, cname, hod):
        self.DeptID = cid
        self.DeptName = cname
        self.DeptHOD = hod
        self.DeptNoOfStud = None
        self.Studs = []
        

class Student():
    def set_name(self,nm):
        Name = nm
        return Name

s = Student()

print(s.set_name("vikas"))



 