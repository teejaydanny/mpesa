l=[11,62,63,46,65,26,17,90]
print(l)
x=int(input("Enter marks"))
print(x)
y=int(input("Enter marks"))
print(y)
if x<=0 or y<=0:
    print("Invalid marks")
elif x>=10 or y>=10:
    print("failed")
elif x<=20 or y>=20:
    print("poor")
elif x<=30 or y>=30:
    print("bad")
elif x<=40 or y<=40:
    print("average")
elif x<=50 or y<=50:
    print("good")
elif x<=60 or y<=60:
    print("excellent")
elif x>100 or y>100:
    print("out of range")








