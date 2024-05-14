# class Magari:
#     def __init__(self, price, name):
#         self.name = name
#         self.price =price
#     def onyesha(self):
#         print(f"my favorie car is {self.name}"
#               f"  and it costs{self.price}")
# myobj=Magari(name="Toyota", price=20000000000)
# myobj.onyesha()
#
#
# #
# # friuts(name,price,type)
# # method
#
# class fruits:
#     def __init__(self, name, price, colour):
#         self.name = name
#         self.price = price
#         self.colour = colour
#     def mpya(self):
#         print(f"my favorie fruit is {self.name}"
#               f" and it costs {self.price}"
#               f" for colour {self.colour} ")
# myobj0=fruits("mango","520",colour="red")
# myobj1=fruits("plums","87",colour="blue")
# myobj2=fruits("pineapple","25",colour="green")
# myobj3=fruits("apple","65",colour="yellow")
# myobj0.mpya()
# myobj1.mpya()
# myobj2.mpya()
# myobj3.mpya()
#
# class employees:
#     raise_amt=5.05
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#         self.email = first_name + "." + last_name + "@gmail.com"
#
#     def full_name(self):
#         return '{} {}'.format(self, self.first_name, self.last_name)
#
#     def apply_raise(self):
#         self.salary = int(self.salary * self.raise_amt)
#
#
# emp1=employees(first_name="Toyota", last_name="veryone", salary=100000)
# emp2=employees(first_name="daniel", last_name="mwangi", salary=1456498)
# print(emp1.first_name)
# print(emp2.first_name)
# print(emp1.email)
# print(emp2.email)
# print(f"")


class Employees:
    second_name = "Juma"
    raise_amount = 1.05
    def __init__(self,name,gender,salary):
        self.name = name
        self.gender = gender
        self.salary =salary
        self.email=name+"@gmail.com"
    def full_name(self):
         return self.name
    def salary_increase(self):
        self.salary =int(self.salary*self.raise_amount)
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
class Developer(Employees):
    def __init__(self,name,gender,salary,program_lang):
        super().__init__(name,gender,salary)
        self.program_lang = program_lang

developer1=Developer("Cynthia","Female",60000,"Python")
developer2=Developer("Cheptoo","Female",60000,"Javascript")
print(f"{developer1.full_name()} develops with {developer1.program_lang}")
print(f"{developer2.full_name()} develops with {developer2.program_lang}")

class Receptionist(Employees):
    def __init__(self,name,gender,salary,Age):
        super().__init__(name,gender,salary)
        self.Age = Age
Rec1 = Receptionist("Makshy","Female",6000,"20")

emp1 = Employees("Felix","Male",100000)
emp2 = Employees("danny","male",200000)
emp3 = Employees("Amy","Female",300000)
print(emp1.name)
print(emp2.name)
print(emp3.name)
print(emp1.email)
print(emp2.email)
print(emp3.email)
print(f" {emp1.name} is {emp1.gender} and earns {emp1.salary}")
print(f" {emp2.name} is {emp2.gender} and earns {emp2.salary}")
print(f" {emp3.name} is {emp3.gender} and earns {emp3.salary}")
print(f"{emp1.name}")
print(emp1.full_name())
print(emp1.salary)
emp1.salary_increase
print(emp2.salary)
emp2.salary_increase()
print(emp2.salary)
emp2.salary_increase()
Employees.raise_amount=3
print(emp1.raise_amount)
print(emp2.salary)
print(emp3.salary)


#practice
class student:
    def __init__(self,first_name,last_name,subject1,subject2):
        self.first_name = first_name
        self.last_name = last_name
        self.subject1 = subject1
        self.subject2 = subject2
    def full_name(self):
        print(f"{student1.first_name} {student1.last_name} has {student1.subject1} and {student1.subject2} marks in two subjects")
        print(f"{student2.first_name} {student2.last_name} has {student2.subject1} and {student2.subject2} marks in two subjects")
student1= student("John","Smith","70","65")
student2= student("Andrew","Johnson","80","50")
print(student1)
print(student2)

#practice2
class Parents:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Child(Parents):
    def __init__(self,name,age,gender):
        self.age = age
        self.gender = gender
        self.name = name
child1 = Child("April","10","Female")
child2 = Child("Keshy","7","Male")

p1 = Parents("Kelvin","22","Male")
p2= Parents("Amy","18","Female")
print(p1.name)
print(p1.age)
print(p1.gender)
print(p2.name)
print(p2.age)
print(p2.gender)





