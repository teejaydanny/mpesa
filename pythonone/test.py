
class parents_staff:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class childs(parents_staff):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

child1 = childs("daniel","21","male")
child2 = childs("samuel","48", gender="Male")

parent1 = parents_staff("miguel","22","Male")
parent2 = parents_staff("haly","56","female")
print(parent1.name)
print(parent1.age)
print(parent1.gender)
print(parent2.name)
print(parent2.age)
print(parent2.gender)



class person1:
    def __init__(self, name, country, year_of_birth,):
        self.name = name
        self.country = country
        self.year_of_birth = year_of_birth

    def age(self):
        today = 2024
        age = today -int(self.year_of_birth)
        return age

p1 =person1("daniel","kenya,",'2003')
print(p1.age())












