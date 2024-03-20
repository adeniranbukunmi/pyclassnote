# python collections (Array)
# list [] or list()
# tuple()   
# set {}
# dictionary (key:value)

# List: IS A COLLECTION WHICH IS ORDERED, CHANGEABLE, ALLOWS DUPLICATE VALUE, AND THEY ARE INDEXED.A list is created with a square bracket [] or list() constructor.

my_list=list(('shade', 'dare', "magret", "femo"))
my_list2 = ['shade', 'dare', 'magret', True, False, 12, 12.234, 'energy', 'energy', [12.000, 'keke', 'fire']]

# my_list3 = [1, 45, 54, 23, 67, 78, 46]
# print(my_list[-1][0])          
# print(type(my_list))
# print(my_list2)
# print(my_list[3])
# print(len(my_list))

# my_list[1] = "solar"   #updating index [1] to solar
# print(my_list)

# print(my_list2[1:5])
# print(my_list2[-3])
# print(my_list2[-4:-1])
# print(len(my_list2))
# print(type(my_list2))

# assignment on list slicing and other methods
# palindrome checker
string = input("Enter a string: ").lower().strip()
split_string=string.split()
join_string="".join(split_string)

if join_string == join_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# if "energy" in my_list:    
#   print("present")
# else:
#   print("not available")

# my_list.append("tunde")
# print(my_list)

# my_list.insert(3, "tunde")  #takes two argument 1.index 2.the data you want to insert
# print(my_list)

# my_list.extend(my_list2)
# print(my_list)
    
# for name in my_list2:
#     my_list.append(name)
# print(my_list)

# print(my_list.index("MAGNET"))
    
# my_list.remove("energy")
# print(my_list)
   
# my_list2.pop()
# print(my_list2)
    
# my_list2.pop(2)
# print(my_list2)
    
# my_list2.clear()
# print(my_list2)
    
# del my_list2
# print(my_list2)
    
# my_list3.sort()
# print(my_list3)
    
# my_list3.sort(reverse=True)
# print(my_list3)
    
# my_list2.reverse()
# print(my_list2)
    
# name = my_list2.copy()
# print(name)
    
# TUPLE
# Tuple: A tuple is a collection that is ordered but not changeable. A tuple is created using
#  braces i.e () or tuple() constructor

names = ("Shade", "energy", "magnet", "Charles", "Energy",('energy','cashew','Babatunde') )
print(names[:-1])
new_name=list(names)
new_name[3] ='Temitayo'            #updating index 3 to Temitayo after conversion
name=tuple(new_name)
print(name)
print(type(name))
name2 = tuple([12, 14, "Sunday", "Charles", True, False, 5.08])     #can take any datatype
print(type(name2))
print(name2)
print(name[3])
print(name[1:4])
print(name[-3])
print(name[-3:-1])

# JOINING TUPLES👇
# new_name = name + list_of_items
# print(new_name, 'after adding')
# # print()
# new_name5 = new_name * 3
# print(new_name5, 'new name after multiplying')
# print()

# method
# print(name.count('energy'))
# print(name.index('Energy'))
# name[3] = "wine" #unchangeable
# name.add("toy") # tuple has no attribute add error
# name.pop() # tuple has no attribute pop error
# name.clear() # tuple object cannot be cleared
# del name
# print(names)

# nested tuple
list_of_items=(('rice', 'mango','tolu'),('maize', 'cherry','Azeez'),('cowpea','cashew','Babatunde'))
print(len(list_of_items))
print(list_of_items[2])

# looping a tuple
# class work build a cbt test application and score the student over 20
# test_question = [
#     ('b', '1. Capaital of Nigeria a) Ijebu b) Abuja'),
#     ('a', '2. Capaital of Lagos a) Ikeja b) Abuja'),
#     ('a', '3. Capaital of Lagos a) Ikeja b) Abuja'),
# ]
# score=0
# for ans, ques in test_question:
#     print(ques)
#     user = input('ans: ')
#     if user == ans:
#         score+=5
#         print('correct \n your score is:',score)
#     else:
#         print('Wrong')

# Unpacking values of a tuple
# item = ("Yam", "Sunday", "Lagos", 45)
list_of_items=(('rice', 'mango','tolu','milk'),('maize', 'cherry','Azeez','milo'),('cowpea','cashew','Babatunde','coco'),  ('maize', 'cherry','Azeez','milo'))
# cereal, *others =list_of_items
# print(cereal)
crop=[]
for food, _, _, _ in list_of_items:
    crop.append(food)
# print(crop, 'our food ')
# print(cereal[0])
# (food, name, location, age) = item  #unpacking each element into new variables
# print(location)
# (food, *others, age) = item      #this '*' means all
# print(others)
# (food, *others) = item
# print(food)
# print(others)
    
item = (("Yam", "Sunday", "Lagos", 45, 'sobo', 'camry' ), ("beans", "bukunmi", "osogbo", 50, 'kunu', 'toyota'), ("rice", "shola", "kenji", 48, 'sobo', 'rolls royce'))
# print(len(item),'loaded')
# for food, name, location, age, drink, cars in item:
#     print("Food:", food)
#     print("Name:", name)
#     print("Location:", location)
#     print("Age:", age)
#     print("drink:", drink)
#     print("car:", cars)
#     print()

# foods = [food for food, _, _, _, _, _ in item]
# print(foods, 'the food i requested')
    
# names = []
# for _, each_name, _, _, _, _ in item:     #using list comprehension
#     names.append(each_name)
# print(names, 'name of people')

# foods = []
# for food in item:
#     foods.append(food[0])
# print("Foods extracted from tuples:", foods)  #this will help access each element at the index specify


# DICTIONARY
# Dictionary: Dictionary is a collection which is ordered, changeable but do not allow duplicate
# Dictionary are used to store data in a key:value pairs.

# It is written using {key:value} or dict(key=value)

# student_record = dict(name="Tony Johnson", level=300, course="mechanical engineering", subjects=10)
# product = {'producer':'Toyota', 'model':'venza 2021', "model":"benz306", 'engine':'6 engines', 'color':'black', 'gear':6, "ok":True}

product={
    "product name":"Toyota",
    "model":"Avallon XX50",
    "year":"2020",
    "engine":"1 engin",
    "color":"dark gray",
    "gear":6,
    "ok":True
}
# nested dict
electronics={
    "item1":{
        "name":"hp",
        'model':'pro book 540',
        'year':{
            'model1':2020,
            'model2':2320,
        }
    },
"item2":{
        "name":"del",
        'model':'pro book '
    },
"item3":{
        "name":"hp",
        'model':'pro book 540'
    },
}

inner=electronics["item1"]['year']['model1']
# electronics.update({'item4':'acer'})
print(inner )
laptop={
    "product name":"hp",
    "model":"pro book 540",
    "inches":15.6,
    "color":"silver",
    "generation":"7th gen",
    "processor":"intel corei7-1355U",
    "ram":"32gb memory",
    "price":"$1199.00"
}

# print(laptop.keys())
# print(len(product))
# print(type(product))
# print(product["color"])
# print(product.get("producer")) 
# print(product.keys())
# print(product.values())
product["persenger"] = 10
# print(product)
# print(product.items())
# print("model" in product)
# product["color"] = "white"
# print(product)
# product.update({"year":2021, "color":"white"})
# product.update(dict(year=2021, color="white"))
# print(product)
# electronics.pop('item1')
# print(electronics)
# electronics.popitem()
# print(electronics)
# del product['model']
# print(product)
# product.clear()
# print(product)
# del product
# print(product)

phone_num = ("enter your phone number>>> ")
digit_mapping = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}
output="" #this is to collect the output
for digit in phone_num:
    output += digit_mapping.get(digit) + " "    #the empty string is for the words not to be too close to each other
# print(f"your phone number read thus\n", output)