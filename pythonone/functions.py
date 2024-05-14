#
# def my_function():
#     text = "Hello World!"
#     print("Hello")
#     print("Hello")
#     print("Hello")
# my_function()
#
# def number_one():
#     number = input("Enter a number: ")
#     print(number)
# number_one()
#
# def number_two(text):
#     text = input("Enter a integer:")
#     print(text)
# number_two("text")


def name(first_name):
    print(first_name)
name('danny')
name('denno')
def student_name(first_name, last_name):
    print(first_name + " " + last_name)
student_name(first_name="danny", last_name="denno"'')

def name(first_name):
    print(first_name)
name('joji')
name('abby')
name('isaa')
def student_name1(first_name,middle_name, last_name):
    print(first_name + " " + middle_name + " " + last_name)
student_name1(first_name="joji", middle_name="denno", last_name="isaa")

def salutation(first_name):
    print(first_name + 'good morning')
salutation('danny')

def salutation(firstname, lastname):
    print(firstname + ' ' + lastname + 'good morning')
# salutation('danny')
salutation('danny', 'joji')
salutation('abby', 'haly')
salutation('davy', 'zack')

def school_age(first_name, age):
    if age<10:
        print(first_name + 'you are young')
    elif age>10 :
        print(first_name + 'you are middle aged')
    else:
        print(first_name + 'you are older aged')
school_age(first_name= 'danny', age=10)
school_age(first_name= 'abby', age=5)
school_age(first_name= 'davy', age=20)


def add_age(age):
    new_age = age + 10
    return new_age
future_age = add_age(20)
print(future_age)



def remove_age(age):
    new_age = age - 10
    return new_age
past_age = remove_age(15)
print(past_age)


def country(nchi ='kenya'):
    return nchi
print(country('norway'))
print(country('china'))
print(country('japan'))
print(country())











