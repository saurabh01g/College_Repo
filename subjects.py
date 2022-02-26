from base_file import BaseClass
class Subject(BaseClass):
    def __init__(self,  subid, subname, is_practical):
        self.SubID = subid
        self.SubName = subname
        self.SubIsPractical = is_practical