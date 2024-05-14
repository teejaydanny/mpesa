Name= input("Enter your name")
a=int(input("Enter the height"))
print(a)
b=int(input("Enter the weight"))
print(b)
BMI= (b/a*2)
print('Your BMI is ',BMI,'Kg/M')
if BMI<=18:
    print('underweight')
elif BMI>=18 and BMI<=24:
    print('normal')
elif BMI>=24 and BMI<=30:
    print('overweight')
elif BMI>=30 and BMI<=50:
    print('abnormal overweight dad')












