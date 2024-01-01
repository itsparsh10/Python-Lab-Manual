class ITM:
    
    def __init__(self):
        self.name = input("Enter your name ")
        self.age = int(input("Enter your age "))
        self.department =int((input("Which department you want in\n1.Pgdm\n""2.Btech\n ")))
        
        
    def display(self):
        if self.department == 1:
            print("*****Btech Department*****")
            print("Name:-",self.name)
            print("Age:-",self.age)
           
        elif self.department == 2:
            print("*****Pgdm Department*****")
            print("Name:-",self.name)
            print("Age:-",self.age)
          

list = []
n = int(input("How many students data you are entrying "))
for i in range(n):
    student = ITM()
    list.append(student)
for student in list:
    student.display()