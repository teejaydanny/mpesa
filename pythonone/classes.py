# class person:
#     age = 32
#     print(age)
# p1 = person()
# print(p1.age)
#
#
#
#
#
#
# class student():
#     grade = 'A'
#     print(grade)
# s1 = student()
# s2 = student()
# s3 = student()
# print(s1.grade)
# print(s2.grade)
# print(s3.grade)
#
#
#
# class employees():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# e1 = employees(name='John', age='31')
# e2 = employees(name='alex', age='56')
# e3 = employees(name='joan', age='20')
# print(e1.age)
# print(e2.age)
# print(e3.age)
#
# class student():
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#         def display(self):
#             print('my name is', self.name)
# s1 = student(name='John',age='31', marks='90')
# print(s1.display())


class parents():
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender =gender
    def display(self ):
            print('my name is', self.firstname)
            print('my name is', self.lastname)
            print('my age is', self.age)
            print('my gender is', self.gender)
p1 = parents(firstname='daniel', lastname='john', age=45, gender='male')
p2 = parents(firstname='samuel',lastname='don',age=56,gender='female')
p3 = parents(firstname='joel',lastname='mary',age=5,gender='male')
p4 = parents(firstname='david',lastname='kiprop',age=21,gender='male')
print(p1. display())
print(p2.display())
print(p3.display())
print(p4.display())

#
# class Person:
# count = 0   # This is a class variable  
#   
#     def __init__(self, name, age):  
#         self.name = name    # This is an instance variable  
#         self.age = age  
#         Person.count += 1   # Accessing the class variable using the name of the class  
# person1 = Person("Ayan", 25)  
# person2 = Person("Bobby", 30)  
# print(Person.count)



# Counting the number of objects of a class
# #
# class Student:    
#     count = 0    
#     def __init__(self):    
#         Student.count = Student.count + 1    
# s1=Student()    
# s2=Student()    
# s3=Student()    
# print("The number of students:",Student.count)




