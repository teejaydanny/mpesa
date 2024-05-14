class Student:
    name = 'Felix'
    age = 16


print(Student.name)
print(Student.age)
print(f'Name: {Student.name} Age: {Student.age}')


class Employees:
    name = 'Felix'
    salary = 1600
    status = 'Married'


print(Employees.name)
print(Employees.salary)
print(Employees)
print(f"Employees name is {Employees.name}"
      f"and he earns a salary of {Employees.salary}"
      f"and he is Married {Employees}")


class Parents:
    first_name = 'John'
    last_name = 'Kimani'


parent1 = Parents()
print(parent1.first_name)


class Parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


parents1 = Parent('felix', 'kimani')
print(f"The first name is {parents1.first_name} and the last name is {parents1.last_name}")
parents2 = Parent('Elix', 'Cheptoo')
print(f"The first name is {parents2.first_name} and the last name is {parents2.last_name}")


class Presidents:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


presidents1 = Presidents('uhuru', 'kimani', 34)
print(f"The first name is {presidents1.first_name} and the last name is {presidents1.last_name} and the age is {presidents1.age}")
