# ❤️STRING attributes and method

#❤️ string can be in single, double or triple quote
# water = 'bottle water'
# print(water)

# i = me = myself = "oluwabukunmi"    #multiple assignment
# print(i)
# print(me)
# print(myself)

X = 20,30,40,50
# print(X)
# print(type(X)," this is x type")

# value = 'Damilare1234@#^2' #can take any datatype
# print(type(value))

story=""" i 
    love ogbomoso mango 
    and i can finish 
        two basket
        ln a sitting"""
# print(story)

# ❤️Accessing characters in string
                        # 0    1    2    3    4    5   
# name = 'sunday, '   #== ['s', 'u', 'n', 'd', 'a', 'y', ',', ' ']
# name2 = 'sunday'
# print(len(name))

greeting ='Welcome'     #string are immutable
# greeting[0]='d'
# print(greeting)   #string dont support assignment
new_greeting=greeting.replace('W', 'd')    #a new variable name is needed
# print(new_greeting) 

# password=8
# user=input('enter a password: ')
# if len(user) > password:
#     print("your own is too much")
# elif len(user) != password:
#     print("not up to eight character")
# else:
#     print("password successful")

name = 'sunday'

# ❤️slicing
# print(name[-3])
# print(name[:2])
# print(name[3:])
# print(name[7])


# comment = "commented that This is a python class. it started last week and still continue through this week. the number of people in this class is"
# print(len(comment))
# print("the length of comment is ", len(comment))

# print(comment[2])
# print(comment[:9])
# print(comment[9:])
# print(comment[15:54])
# print(comment[-20])
# print(comment[-37:-3])


# String Method
comment = "commented that This is a python class. it started last week and still continue through this week. the number of people in this class is"
# endswith()
# print(comment.startswith("commented that"))
# print(comment.endswith("class is"))

# email validator


# Strip() function
# name2 = "     shade  daniels"
# print('length before strip is ', len(name2))
# print('length after strip is ', len(name2.strip()))

# eg
# user = input("USSD Code: ")
# if user.strip() == '*310#':
#     print('welcome')
# else: 
#     print('invalid input')

# capitalize(), lower(), upper() function

# order = input("What do you want eat? ")
# print(order.upper())

# if order.strip().capitalize() == "Rice":
#     print("success")
# else:
#     print("failed")

# Lower() function
# name = 'SUNDAY'
# print(name.lower())

# how split () works: 
# story=input("tell us a story: ")
# splitted_story=story.split('mango')
# print(splitted_story)
# print(splitted_story[0])

# using split () to create acronym
# user_input = str(input("Enter a Phrase: "))
# text = user_input.split()
# print(text)
# a = " "
# for i in text:
#     a = a+str(i[0]).upper()
# print(a)

#assignment(weight converter app) note:capitalize wont work because it deals with the first letter and here we are working with int and char

# weight=(input("enter your weight  in Kg or Lbs for pounds>>> ")).upper()
# if weight.endswith('KG'):
#     splitted_weight=weight.split('KG')
#     print(splitted_weight)
#     converted_to_int=int(splitted_weight[0])
#     converted_weight= converted_to_int / 0.453
#     converted_weight=round(converted_weight, 3)
#     print(f'your weight in pounds is {converted_weight}lbs')
# elif weight.endswith('lbs'):
#     splitted_weight=weight.split('lbs')
#     converted_to_int=int(splitted_weight[0])
#     converted_weight= converted_to_int * 0.453
#     converted_weight=round(converted_weight, 3)
#     print(f'your weight in kg is {converted_weight}kilos')

# else:
#     print('Error: Please provide weight in either kg or lbs.')


# Replace() function
# newval = comment.replace("commented", "stated")
# print(comment)
# print(newval)

comment = "commented that This is a python class. it started last week and still continue through this week. the number of people in this class is"
# Split() function
# print(comment.split())
# print(comment.split('.'))
# print(comment.lower().split('this'))
# Join() function
word_split = comment.split()
# print(word_split)   
# print(" ".join(word_split))
# value = ["rice", "beans",                                                              "yam", "banana"]
# print(" is ".join(value)+" >>>> this is the new joining")

# Capitalize() function
# name = "     sunday adeniran"
# print(name.capitalize())
# print(comment.capitalize())
# comment.capitalize()

# Center() function
# name = "tim bank"
# print(name.center(80))

# Count() function
# print(comment.count(""))

# Escape character (\)
# print('she\'s the owner')
# print('she is the\b owner')
# print('she is the\t owner')
# print('she is the\n owner')

