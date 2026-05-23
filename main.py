class Students:
    def ___init___(self,name,grade,age,club):
     self.name=name
     self.grade=grade
     self.age=age
     self.club=club
     
     def display(self):
        print(f"Name:{self.name}\nGrade: {self.grade}\n Age: {self.age}\nClub:{self.club}")

name=input("enter name: ")
age=int(input("enter age: "))
grade=int(input("enter grade: "))
club=input("enter club: ")

student1=Students(name,age,grade,club)
student1.display()