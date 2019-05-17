#!/bin/python3

#print strings
print("stringBasics:")
print('hello using single quotes')
print("""multi line
comments using triple quotes""")

#math
print('\n') #new line
print('Math time:')
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents 50 raised to power 2
print(50 % 6) #modulo
print(50 // 6) # number without lefovers

# Variables & methods
print('fun with variables and methods:')
quote = 'All is fair in love and war'
print(len(quote)) # length of the string
print(quote.upper()) # convert to upper case
print(quote.lower()) # convert to lower case
print(quote.title()) # convert to title case

print('\n') #new line

name = 'Kalimoh'
age = 21 # int can also be written as int(21)
gpa = 3.9 # float can also be written as float(3.9)

print(int(age))
print(int(21.9)) #this will print only the number before the decimal and ignores the number after decimal

#print('my name is '+ name + 'and I am' + age + ' years old') # this will error out as age is not converted to string
print('My name is '+ name + ' and I am ' + str(age) + ' years old') # converted int to string

print('\n') #new line
age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n') #new line

#Functions **********************************
def new_line():
	print('\n')
new_line()

print('Now some functions: ')
def who_am_i():
	name1 = 'Saty'
	age = 29
	print('My name is '+ name1 + ' and I am ' + str(age) + ' years old') # converted int to string

who_am_i()	#we can't use the variable name1 to print the name as it is defined inside a function and can't be accessed outside it.

new_line() #new line
#adding parameter
def add_one_hundred(num):
	print(num+100)
add_one_hundred(100) # This will return 100 + 100

new_line() #new line
#Add multiple parameteres
def add(x,y):
	print(x+y)

add(7,5)
add(209,313)


new_line() #new line
#using return
def multiply(x,y):
	return x*y
print(multiply(7,7))

def square_root(x):
	return x ** .5
print(square_root(49))

new_line() #new line
#Boolean Expressions (True or False)
print('lets check boolean now: ')
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)

new_line() #new line

print(type(bool2))

# Relational and boolean operators
greater_than = 7>5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7 > 5) and (5 < 7)
test_or = (7 > 5) and (5 < 7)
test_not = not True

print(test_and)

#CONDITIONAL STATEMENTS
print('Conditional statements: ')
def soda(money):
	if money >= 2:
		return "You have got yourself a soda!"
	else:
		return "No soda for you!"
print(soda(3))
print(soda(1))


new_line()
def alchol(age,money):
	if (age>=21) and (money>=5):
		return "someones getting drunk!"
	elif (age<21) and (money>=5):
		return "You are underage"
	elif (age>=21) and (money<5):
		return "you have less money!"
	else:
		return "You are under age and don't have money"

print(alchol(21,5))
print(alchol(20,5))
print(alchol(21,4))
print(alchol(20,4))

new_line()

#Lists
print("lists have brackets: [] …………………………………….")
movies = ['movie1', 'movie2','movie3','movie4']

print(movies[0])
print(movies[0:3]) #means movies at postion 0 to 2 will be printed

print(movies[1:]) #slicing starting from 1
print(movies[:1]) # slicing upto 1
print(movies[-1]) #prints last item in the list
print(len(movies))

movies.append('jaws')
print(movies)

movies.pop() #removes the last item in the list
print(movies)

movies.pop(1)
print(movies)

movies = ['movie1', 'movie2','movie3','movie4']
person = ['person1','person2','person3','person4']
combined = zip(movies , person)
print(list(combined))

new_line()

#tuples - can't add new or pop an existing 
print('tuples hav parantheses and cannot change')
grades = ('a','b','c')
print(grades[1])

#Looping
print('For loops - start to finish of iterate: ')
movies = ['movie1', 'movie2','movie3','movie4']

for x in movies:
	print(x)

new_line()

print('now the while loop - *Execute as long as true*: ')
i=0
while i<10:
	print(i)
	i+=1	
