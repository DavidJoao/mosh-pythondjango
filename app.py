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

#Type conversion
birth_year = input('Birth year: \n')
age = 2020 - int(birth_year)
print(age)
pounds = input('Enter your weight in pounds: \n')
kilograms = float(pounds) * 0.45
print ('Your weight in kilograms is ' + str(kilograms))

##String methods
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


