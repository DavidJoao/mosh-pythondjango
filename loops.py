# #########################################      While loops
#while condition: run loop
#Example:

i = 1
while i <= 5:
    print(i)
    i += 1

# #Guessing game using While Loop

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
    
#########################################      For Loops

example = 'Python'
for item in example:
        if item == 'o':
            item = 'x'
        print(item)
# or
for item in range(10):
    print(item)

#if we want to set a specific range we can do something like this:
for item in range (7, 10): #we can add a third argument to modify how many steps are taken by iteration
    print(item)

prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(f"The total is {total}")

#########################################      Nested Loops

# for x in range(4):
#     for y in range (3):
#         print(f"({x}, {y})")

numbers = [2, 2, 2, 2, 5]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)