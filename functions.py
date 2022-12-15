#########################################      Functions
#We are going to use functions when we are required to perform a task multiple times
#Example #1
def greet_user():
    print('Hey there!')
    print('Welcome aboard!')


#After defining a function, we need to let two lines between the function and the following code
#Adding parameters allows us to make more custom functions like this one:
def greet_person(name, last_name):
    print(f'Hey {name} {last_name}, how are you?')


#You need to pass the parameter when calling the function
greet_person('David', 'Sandoval')

#########################################      Keyword Arguments
#Keyword arguments are used to make code more readable when calling functions, for example:
greet_person(name="David", last_name="Sandoval") #Output will be the same, but now we know what arguments represent each String



#########################################      Return Statements
def square(number):
    return number * number
#returns a value, so we can assign it to a variable
square_of_three = square(3)
print(square_of_three)


#########################################      Creating Re-usable functions
def converter(message):
    message_array = message.split(" ")
    final_message = ''
    emojis = {
        ":)" : "😀",
        ":(": "😞",
        "tinker": "🐶",
        "que": "🧀"
    }
    for word in message_array:
        final_message += emojis.get(word, word) + " "
    return final_message


print(converter('Nooo tinker que :('))

#########################################      Exceptions
try:
    age = int(input('Age: \n'))
    print(age)
except ValueError:
    print('Invalid value')
