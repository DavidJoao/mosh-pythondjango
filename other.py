#########################################      Dictionaries
#In a dictionary we can store a bunch of key value pairs
customer = {
    "name": "David Sandoval",
    "age": 23,
    "is_verified": True
}
#Each key should be unique
#Values can be strings, numbers, boolean, lists
customer["name"] #should return "David Sandoval"
print(customer["name"])

#Exercise
phone = input('Phone: \n')
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}

output = ""
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)


message = input(">")
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
print(final_message)

