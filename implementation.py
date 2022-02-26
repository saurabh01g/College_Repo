from college import College
from department import Department
from students import Student
from subjects import Subject
from utility import generate_students
from base_file import BaseClass
import random
c1 = College(cid=112211, cname="Dy Patil", princi="Dr. Patil", no_of_stud=45)

d1 = Department(cid=654987, cname="IT", hod="Abc") 
d2 = Department(cid=654997, cname="CS", hod="Xyz") 
d3 = Department(cid=654564, cname="Etx", hod="Lml") 
d4 = Department(cid=654626, cname="Mech", hod="Opd")

c1.Departments.extend([d1, d2, d3, d4])

studs = generate_students(45, Student)

d1.Studs.extend(studs[0:8])
d2.Studs.extend(studs[8:18])
d3.Studs.extend(studs[18:30])
d4.Studs.extend(studs[30:46])


depts = [d1, d2, d3, d4]

for d in depts:
    d.DeptNoOfStud = len(d.Studs)

subj_list = ["Chemistry", "Physics", "Maths", "English", "Mechanics"]

sub1 = Subject(subid=701, subname=subj_list[0], is_practical=True)
sub2 = Subject(subid=702, subname=subj_list[1], is_practical=True)
sub3 = Subject(subid=703, subname=subj_list[2], is_practical=False)
sub4 = Subject(subid=704, subname=subj_list[3], is_practical=False)
sub5 = Subject(subid=705, subname=subj_list[4], is_practical=True)

list_of_subjs = [sub1, sub2, sub3, sub4, sub5]

random.shuffle(list_of_subjs)

for i in studs:
    random_subs = list_of_subjs[0: random.randint(1, 5)] # 5
    i.StudSubjects.extend(random_subs)

print(studs)
# ########Student name whos initial letter is a#####################
def get_stud_with_initial(initial):
    for i in studs:
        if i.StudName[0]== initial:
            print(i.StudName)

get_stud_with_initial("A")
# ##################################################################


#####Average marks of all students whos Subject is chemestry#####
def get_avg_marks(subj):
    sum = 0
    count=0
    for i in studs:
        for sub in i.StudSubjects:
            if sub.SubName == subj:
            # print(i.StudMar)
                sum+= i.StudMar
                count+=1
    avg =sum/count
    print("Average of Marks of all students with subject Chemsitry :",avg)
get_avg_marks("Chemistry")
##############################################################################################


#####count student who has 4 subject###########################33
def get_stud_count(noofsubj):
    countstud =0
    for i in studs:
        if len(i.StudSubjects) == noofsubj:
            countstud+=1
    print(f"Student who has {noofsubj} subject:",countstud)
get_stud_count(4)
##############################################################

######Stud list with marks greater than 50##################
def get_stud_list_wtih_greater(marks1):
    stud_list2 =[]
    for i in studs:
        if i.StudMar>marks1:
            stud_list2.append(i.StudName)
    print("Student who has marks greater than 50: ",stud_list2)
get_stud_list_wtih_greater(50)

