my_dictionary = {
    "Name": "danny",
    "gender": "male",
    "birthday": "1970-01-01"
}

my_dictionary = dict(
    Name="danny",
    gender="male",
    birthday="1970",


)
print(my_dictionary)


my_dictionary={
    "Name":"Felix",
    "Gender":"Male",
     "Status":"Single"
}
print(my_dictionary)

my_dictionary=dict(
    Name="Felix",
    Gender="Male",
    status="Single"
)
print(my_dictionary)
print(my_dictionary["Gender"])#print specific dictionary value
print(my_dictionary.get('Status'))#prints
my_dictionary['Status']="Complicated"#edits dictionary value
print(my_dictionary)
my_dictionary['BirthDate']=2005 # adds key,
print(my_dictionary)
my_dictionary2=my_dictionary.copy()
print(my_dictionary2)
print(my_dictionary)
print(len(my_dictionary))
my_dictionary.pop('Status') #removes a dictionary
print(my_dictionary)
del my_dictionary2['Status']
print(my_dictionary2)
my_dictionary.clear()
print(my_dictionary)
del my_dictionary
print(my_dictionary2)
if "Name" in my_dictionary2:
    print("Name found")
else:
    print("Name not found")

for value in my_dictionary2:
    print(my_dictionary2[value])

for key in my_dictionary2:
    print(key)

    for key, value in my_dictionary2.items():
        print(key, value)

my_dictionary3={
    "Item":"Soaps",
    "Price":"two hundred",
    "Quantity":'2'
}
print(my_dictionary3)
my_dictionary3['Quality']='80%'
print(my_dictionary3)
if "Item" in my_dictionary3:
    print("Item found")
else:
    print("Item not found")






