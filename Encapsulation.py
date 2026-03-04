class student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks

    def show_marks(self):
        print("Marks : ",self.__marks)
    
s=student("Niteesh",90)

print("Name : ",s.name)

s.show_marks()

'''

class student():
    def __init__(self,name,rollno,marks):
        self.name=name
        self._rollno=rollno
        self.__marks=marks
s=student(name="niteesh",rollno=65,marks=90)
print(s.name)
print(s._rollno)
print(s._student__marks)

'''