#Types of variables
price = 10 #integer
rating = 3.6 #float
name = 'David' #string
is_published = False #boolean

#Exercise 1
patient_name = 'John Smith'
age = 20
new_patient = True

the_name = input('What is your name? \n')
fav_color = input('What is your favorite color? \n')
print('Hi ' + the_name + ', I see your favorite color is ' + fav_color)

# Type conversion
birth_year = input('Birth year: \n')
age = 2020 - int(birth_year)
print(age)
pounds = input('Enter your weight in pounds: \n')
kilograms = float(pounds) * 0.45
print ('Your weight in kilograms is ' + str(kilograms))

#String methods
course = 'Python for beginners'
print(len(course)) #Prints length of string
course.upper() #Makes string uppercase, doesnt modify original string
course.find('f') #finds index of character
'Python' in course #returns boolean 

x = 2.9
round(x) #rounds up to 3
abs(x) #returns always positive
#there also exist ceil and floor methods

#If statements
is_hot = False
is_cold = False

if is_hot: 
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else: 
    print('Lovely day')

house_price = 1000000
good_credit = False

if good_credit:
    print(house_price + (house_price * 0.10))
elif good_credit == False:
    print(house_price + (house_price * 0.20)) 

#Logical Operators
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit: #Instead of 'and' operator, we can use the 'or' operator, which checks if one of two applies
    print('Eligible for loan')
else:
    print('Not eligible for loan')

#Comparison Operators
#They are useful for comparing variables with value, for example comparing a variable 'temperature' > 30
#Different comparison operators are >, <, <=, >=, ==, !=
temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = 'David'
if len(name) < 3: 
    print('Name needs to contain more than 3 characters')
elif len(name) > 50:
    print('Maximum characters exceeded')
else:
    print('Name looks good')

#While loops
#while condition: run loop
#Example:

i = 1
while i <= 5:
    print(i)
    i += 1

#Guessing game using While Loop
secret_number = 6
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input('Guess the correct number between 0 and 10 \n'))
    guess_count += 1
    if guess == secret_number:
        print('Correct number!')
        break
    else: 
        print('Wrong number')
else:
    print('Sorry, you failed :(')

#Car exercise
answer = ''
is_started = False
print('start - to start the car')
print('stop - to stop the car')
print('quit - to exit')
print('help - to see commands')
while answer != 'quit':
    answer = input('Enter command: \n')
    if answer == 'start':
        if is_started == False:
            is_started = True
            print('Car started!')
        elif is_started == True:
            print('Car already started!')
    elif answer == 'stop':
        if is_started == False:
            print('Already stopped!')
        elif is_started == True:
            is_started = False
            print('Car stopped!')
    elif answer == 'quit':
        break
    elif answer == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        help - to see commands
        """)
    else:
        print("Sorry, I don't understand that command")
    

