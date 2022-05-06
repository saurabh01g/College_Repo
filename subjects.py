from base_file import BaseClass
class Subject(BaseClass):
    def __init__(self,  subid, subname, is_practical, marks):
        self.SubID = subid
        self.SubName = subname
        self.SubIsPractical = is_practical
        self.Marks = marks

        