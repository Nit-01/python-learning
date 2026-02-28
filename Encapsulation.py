class student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks

    def show_marks(self):
        print("Marks : ",self.__marks)
    
s=student("Niteesh",90)

print("Name : ",s.name)
s.show_marks()