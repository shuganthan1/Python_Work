print("Hello")
#create a variable
#x = 1''fg = 'John'
'''
name='john'
print(name)

a=1
b=2
c=3.5
hi = 'hello world'
print(hi)

print('what is your name')
name = input()
print('Hi')
print(name)
'''

# print(what is your first name)
# name =input('what is your name: ')
# # print(What is you age)
# age = input('what is your age ')
# address =input('what is your address ')
# print('Your name is'+' '+ name + '. ' + 'You are '+ age + '. '+ 'You live at '+ address+ '. ')

# a = 24
# b = 16
# print(a+b)
# print(a-b)
# print(4*'me') #multiply
# print(8%3) #gives the remainder
# FLoatNum = 1.356
# IntNum = 4
# name = 'xyz'
# print(FLoatNum + IntNum)
# print(str(IntNum) + name) #turn integer to string type
#
# Single_quotes = 'Look! single quotes'
# Double_quotes = "Look! double quotes" #no diff between quotation marks
#
# String_failure = 'I said 'Wow!''
# escape_example_1 = 'I said \'Wow!\''
# Quote_in_quote = 'I said "wow!"'
# Reverse_quote_in_quote = "i said 'wow!'"
# print(escape_example_1)
# print(Quote_in_quote)
# print(Reverse_quote_in_quote)

#slicing strings
# Hw = "hello! World"
# print(HW[7:]) first leter is 0
# print(Hw[:5]) starts on 0th location
# print(len(Hw)) #includes space in between

#string methods
# White_space = "lot's of space at the end                                                 "
# print(len(White_space))
# print(len(White_space.strip()))

#Example_text = "here's some text with lot's of text"
#count a substring within a string
#print(Example_text.count('text')) # finds the string in the sentence

#lowercase
#print(Example_text.lower())
#uppercase
#print(Example_text.upper())

#capitalise first letter in sentence
#print(Example_text.capitalize())
#replacing text
#print(Example_text.replace('with ', ', '))

#concatenation
# a='here '
# b='more '
# c= 'much more'
# d=10
# print(a+b+c,+d)

#casting
# x=2
# y=5.4
# z='hello'
# print(str(x)+str(y)+z)

#string to numeric casting
# int_string = '6'
# print(int(int_string))
# print(type(int(int_string)))

#boolean
# a = True #true is 1
# b= False  #false is 0
# print(a==b) single equal sign - to assign a value, == - for comparision
# print(a != b)
# print(a >=b)
# print(b<=a)

# print(True and False)
# print(True or False)

#boolean methods within strings
# hi = 'hello world!'
# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith('!'))
# print(hi.startswith('H'))

#boolean values and numbers
# x=-1
# y=2
# print(bool(x))
# print(bool(y))
# print(bool(None))

# txt = "Hello World" [::-1]
# print(txt)
#
# s = 'radar'
# if s==s[::-1]:
#      print(s + ' is a palindrome')
# else:
#     print (s + 'is not a palindrome')
#list  -is a collection which is ordered and changeable. Allows duplicate members.
shopping_list = ['eggs', 'bread', 'banana', 'biscuits','milk'] #list in square bracket
# print(type(shopping_list))
# print(shopping_list[0])
# print(shopping_list[-1]) #-1 always last option counts backwards
# shopping_list[1] ='Roti'  #replace the second on list
# print(shopping_list)

# shopping_list.pop() #removes last item or can add what i want to remove in the brackets
# print(shopping_list)
# shopping_list.append('ice cream') #add to list
# print(shopping_list)
# print(len(shopping_list))

#mixed data type list
# mixture = [1,2,'one']
# print(mixture)
#
# #list slicing
# print(mixture[1:3])
# print(mixture[-2::]) start from 2nd item at the end
# print(mixture[-2::-1])

# print('hello')
# a=10
# b=20
# if (a>b):
#     print('a is bigger than{}'.format(a,b)) # values of a and b go in the gap
# else:
#     print('b is bigger than {}'.format(b,a))

# a= input('give a number: ')
# b = input('give the second number: ')
# c = input('give the third number: ')
# if (a>b and a>c):
#     print ('A is the bigger than {},{}'.format(b,c))
# elif (b>a and b>c):
#     print('B is the bigger than {},{}'.format(a,c))
# else:
#     print('C is the bigger than {},{}'.format(a,b))
#tuples
#essentials - ('bread','egg', 'milk')

# list_data = [1,2,3,4,5]
# for i in list_data:
#     print(i *2)
#declare a list of 10 numbers
#have a check condition like if a<15
#if the condition is satisifed write it to another list and print the list

# list = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# for num in list:
#     if num <5:
#         list2.append(num)
#     else:
#         continue
# print(list2)
#
#
#
# if

# list3 =[10,13,56,64,33,78,33]
# # check whether it is odd or even assing them to diff lists
# # all odd numbers shoud go to odd list
# # all even numbers go to even list
# evenlist = []
# oddlist = []
# for number in list3:   #use loop to go thru each number
#     if number %2 == 0:
#      evenlist.append(number)
# else:
#     oddlist.append(number)
# print(evenlist)
# print(oddlist)

#tuples
#tuples is collection which is ordered and unchangeable and allows duplicate members

# essentials = ('bread', 'eggs','milk')
# print(essentials)
# print(essentials.count('bread'))
#
# essentials[0] = 'beans'

#dictionaries
#is a collection which is unordered, changeable and indexed. We use curly bracket
#have keys and values. easy to pull out data stored in dictionary , used in webdata
student_1 = {
    'name': 'susan',
    'stream': 'tech',
   'completed_lessons':4,
   'completed_lesson_names': ['variables','data_types','set up']
}

# print(student_1)
# print(student_1['stream'])
# print(student_1['completed_lesson_names'][1])

#changing a value
# student_1['completed_lessons'] = 3
# print(student_1['completed_lessons'])
# print(student_1)

#removing an item
# student_1['completed_lesson_names'].remove(('data_types'))
# print(student_1['completed_lesson_names'])

#set
#is a collection which is unordered and unindexed. Sets are written with curly brackets
# car_parts = {'wheels', 'doors', 'exhaust'}
# print(car_parts)
# car_parts.add('windows')
# print(car_parts)
# car_parts.discard('doors')
# print(car_parts)

#frozen sets
#immutable versions of the set similar to tuple ,e.g. dob
# x = frozenset([1,2,3,4])
# print(type(x))

#control flow - flow a sequence
#if statements, for statements and while loops
# age = 19
# if age>19:
#     print('your are the correct age to watch this film and buy a ticket')
# else:
#     print("i'm afraid you are not the correct age to watch this film")

# age = int(input('input your age'))
# if age >18:
#     print('your are the correct age to watch this film and buy a ticket')
# elif age <18:
#     print ("i'm afraid you are not the correct age to watch this film")
    #nested if when more than 2 conditions use elif and end with else


# film_rating = input('what is the film rating? ')
# if film_rating.lower() == "universal":
#       print("all age groups can watch this film")
# elif film_rating == "pg":
#     print("General viewing, but some scenes may be unsuitable for young children.")
# elif film_rating == "12" or film_rating == "12a":
#     print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
# elif film_rating.lower() == "15":
#     print("No one younger than 15 may see a 15 film in a cinema.")
# elif film_rating.lower() == "18":
#     print("No one younger than 18 may see an 18 film in a cinema.")
# else:
#     print("this is not a correct rating, please use unniversal, pg, 12, 12a, 15, 18")

#exericse - fizzbuzz
#if number is divided by 3 print Fizz, it is divided by 5 print Buzz,
#if it is divided by both print Fizzbuzz

#for fizzbuzz in range(51):
# number = int(input('What number? '))
# if number % 3 == 0 and number % 5 == 0:
#         print("Fizzbuzz")
# elif number % 3 == 0:
#         print("Fizz")
# elif number % 5 == 0:
#         print("Buzz")
# else:
#         print('not fizzbuzz')

#for loop
# fruits = ['apple','banana', 'cherry']
# for x in fruits:
#   print(x)
# # for x in 'banana':    #checks each character
# #     print(x)
#   if x == 'banana':
#     break
#
# for x in range(6):
#     print(x)

# adj =['red','big', 'tasty']
# fruits = ['apple','banana','cherry']
# for x in adj:
#     for y in fruits:
#         print(x,y)

list_data = [1,2,3,4,5]
embedded_lists = [[1,2,3],[4,5,6]]

# for num in list_data:
#     print(num*2)

# for data in embedded_lists: #loop of collecting numbers
#     print(data)
#     for num in data:
#         print (num)
# dict_data = {1:{'name':'Bronson','money':'$0.05'},2: {'name':'Masha','money':'$3.66'},3:{'name':'Roscoe','money':'$1.14' }}
# for value in dict_data:
#     print(value) #prints outer value - 1,2,3
#
# for item in dict_data.values():
#     print(item)
# for item in dict_data.values():
#     for embed_value in item.values():
#         print(embed_value)   #nested loops

#while loop
#initialising the variable
x=0
#condition
# while x<10:
#     print(f"its working --> {x}")
#     x=x+1

# while x<10:
#     print(f'its working --> {x}')
#     if x ==4:
#         break
#     x=x+1

