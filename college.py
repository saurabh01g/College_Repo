from base_file import BaseClass
class College(BaseClass):
    def __init__(self, cid, cname, princi, no_of_stud):
        self.ClgID = cid
        self.ClgName = cname
        self.ClgPrinci = princi
        self.ClgNoOfStud = no_of_stud
        self.Departments = []
  
if __name__ == "__main__":
    c1 = College(cid=112211, cname="Dy Patil", princi="Dr. Patil", no_of_stud=450)
    print(c1)

