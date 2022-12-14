#########################################      Lists

names = ['John', 'Bob', 'David', 'Sarah']

print(names)

another_list = [1, 7, 15, 1, 7, 1, 5]
max = another_list[0]
for number in another_list:
    if number > max:
        max = number
print(max)

#########################################      Two Dimensional Lists

#Example of a 3x3 Matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_max = matrix[0][0]
for eachlist in matrix:
    for eachnumber in eachlist:
        if eachnumber > matrix_max:
            matrix_max = eachnumber
print(matrix_max)

#########################################      Lists Methods or Functions

new_list = [5, 1, 6, 5, 10, 8, 10, 26]
new_list.append(20) #inserts item at the end of list
new_list.insert(2, 3) #inserts item in specific index of list, first argument represents index and second argument represents the item inserted
print(new_list)
uniques = []
for number in new_list:
    if number not in uniques:
        uniques.append(number)
print(uniques)
    

#########################################      Tuples
#Tuples are very similar to lists
#Tuples are very strict and we are not able to modify them
#The only two methods that we are able to use are count and index
#We are only able to get information from Tuples

numbers = (1, 2, 3)
numbers.count(1)
numbers.index(1)

#########################################      Unpacking
coordinates = (1, 2, 3)

#This example is a bad practice because it gets too long and repetitive
coordinates[0] * coordinates[1] * coordinates[2] 

#this example
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
#is the same thing as:
x, y, z = coordinates 
#We can use this with lists

