import random
def get_random_name():
    s = ""  # XWH
    for i in range(random.randint(4, 10)):  
        c = chr(64 + random.randint(1, 26))
        s += c
    return s.title()

def generate_students(no, cls_nm):
    stud_list = []
    for i in range(1, no+1):
        s = cls_nm(sid=100+i, sname=get_random_name(), sage=random.randint(19, 26), smarks=random.randint(25, 100))
        stud_list.append(s)
    return stud_list
