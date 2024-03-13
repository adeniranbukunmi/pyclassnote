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
