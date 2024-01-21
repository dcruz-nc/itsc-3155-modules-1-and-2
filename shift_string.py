user_input = input("Enter a string: ")

lowercase = ""
uppercase = ""

for char in user_input:
    if char.islower():
        lowercase += char # add char to lowercase set
    
    elif char.isupper():
        uppercase += char # add char to uppercase set

result = lowercase + uppercase # combine lowercase and uppercase set

print(result)