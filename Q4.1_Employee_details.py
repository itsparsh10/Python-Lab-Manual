# 4.1 Write a program to Create Employee Class & add methods to get employee details & print.
class Employee:
    def __init__(self,name,employee_id,age,number,department,salary):
        self.name = name
        self.employee_id = employee_id
        self.age = age
        self.contact_no = number
        self.dept = department
        self.salary= salary
        
    def display_details(self):
        print(" Your Name Is :",self.name)
        print(" Your ID is :",self.employee_id)
        print(" You are :",self.age," Years Old")
        print(" Contact Number :",self.contact_no)
        print(" Department : ",self.dept)
        print(" Salary : ",self.salary)
        
      
        

b=Employee("Rahul",1234,23,8923134323," Sales ",1000000)
print("\n\n Details of Employee \n ")
b.display_details()

        
            