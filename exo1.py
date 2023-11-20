# # Get user input
# user_input = input("Enter the word 'Bonjour': ")

# # Check if the input is 'Bonjour'
# if user_input.lower() == "bonjour":
#     # Reverse the input and print the result
#     reversed_word = user_input[::-1]
#     print("Reversed:", reversed_word)
# else:
#     print("Invalid input. Please enter 'Bonjour'.")

# user_input1 = input("Enter something: ")
# print("You entered:", user_input1)


user_input2 = input("Enter the word 'Bonjour': ")

# Check if the input is 'Bonjour'
if user_input2.lower() == "bonjour":
    # Reverse the input without using slicing or reversed()
    reversed_word1 = ""
    for char in user_input2:
        reversed_word1 = char + reversed_word1
    print("Reversed:", reversed_word1)
else:
    print("Invalid input. Please enter 'Bonjour'.")
    
prompt = "bonjour je suis ici"
test = list(prompt)
result =""

# Correcting the variable name to 'test'
count = len(test)

# Correcting the range in the for loop
for i in range(count):
    result = result + test[count-(i+1)]
    print (result)
    # print(test[i])


    
