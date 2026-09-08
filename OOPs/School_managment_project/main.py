# it is a school managment system to mannage deta of student and teacher.

import json
from abc import ABC,abstractmethod
from pathlib import Path


deta = {"Students": [], "Teachers":[]} # it is dictionary hear we have deta student and teacher in dict form.

with open("schooldeta.json", "r") as f:
    r_deta = f.read()
    if r_deta:
       deta = json.loads(r_deta)
    else:
        deta = {"Students": [], "Teachers":[]}

def save():
    with open("schooldeta.json", "w") as k:
        json.dump(deta, k, indent=4)

def validate_mail(gmail):
    if "@" in gmail and "." in gmail:
        return True

def exit_rollno(rollnumber):
    exist = False
    for i in deta["Students"]:
        if i["Roll number"] == rollnumber:
            exist = True
            break
    return exist
def tech_exitst(ID):
    exist = False
    for i in deta["Teachers"]:
        if i["Employ Id"] == ID:
            exist = True
            break
    return exist


class person(ABC):

    @abstractmethod
    def rg(self):
      pass
    @abstractmethod
    def get_dt(self):
        pass
    @abstractmethod
    def update_gd(self):
        pass

class students(person):
    def rg(self):
        name = input("Enter you name: ")
        roll_n = int(input("Enter you roll number: "))
        mail = input("Enter you mail hear:  ")
        grade = {"physics": None,
                 "chemistry": None,
                 "math": None}

        if not validate_mail(mail):
            print("Invalid mail Run program again......")
            return

        for i in deta["Students"]:
         if i["Roll number"] == roll_n:
            print("Student roll number already exist. re run the program.. ")
            return
            

        deta["Students"].append(
            {
                "name_student": name,
                "Roll number": roll_n,
                "Student_mail": mail,
                "Grade": grade
            }
        )
        save()
        print("you registration has succesfull")

    def update_gd(self):
        roll_n = int(input("Enter you roll number to update you grade:  "))
        exitstance = exit_rollno(roll_n)
        if exitstance:
            print("Student exit....")
        else:
            print("Student dose not exitst....")
            return

        for i in deta["Students"]:
            if i["Roll number"] == roll_n:
               sub_name = input("Enter you subject name: ")
               sub_mark = int(input(f"Enter your marks in {sub_name}"))
               i["Grade"][sub_name] = sub_mark
        save()
        print("your subject addion is succesfull")


    def get_dt(self):
        roll_n = int(input("Enter you roll number to update you grade:  "))
        exitstance = exit_rollno(roll_n)
        if exitstance:
            print("Student exit....")
        else:
            print("Student dose not exitst....")
            return

        for i in deta["Students"]:
            if i["Roll number"] == roll_n:
              print(i)
        

class techers(person):
    def rg(self):
        name = input("Enter you name: ")
        subject = input("Enter you subject which you teach: ")
        mail = input("Enter you email hear:  ")
        emp_id = int(input("Enter you employ ID: "))

        if not validate_mail(mail):
            print("Invalid mail Run program again......")
            return
        for i in deta["Teachers"]:
            if i["Employ Id"] == emp_id:
                print("this employ id is already exit re rum the program")
                return
        deta["Teachers"].append(
            {
                "Name_techer": name,
                "Employ_mail": mail,
                "Employ Id": emp_id,
                "subject tech": subject
            }
        )
        save()
        print("you registration has succesfull")

    def get_dt(self):
        ID = int(input("Enter you employ ID:  "))
        exitance_tech = tech_exitst(ID)
        if exitance_tech:
            print("Teacher exist you deta is....")
            for i in deta["Teachers"]:
                if i["Employ Id"] == ID:
                    print(i)
        else:
            print("Teacher no found Check ID again and rerun program...")




    def update_gd(self):
        pass


print("Enter one(1) to register STUDETN:-- ")
print("Enter two (2) to register TECHER:-- ")
print("Enter three (3) to add grade of STUDENT:-- ")
print("Enter four (4) to print DETAIL of STUDENT:--")
print("Enter five (5) to print DETAIL of TEACHER")


student = students()
tech = techers()
choise = int(input("Enter you choise:  "))
if choise == 1:
    student.rg()
if choise == 2:
    tech.rg()
if choise == 3:
    student.update_gd()
if choise == 4:
    student.get_dt()
if choise == 5:
    tech.get_dt()