# class Dog:
#     # Class variable
#     species = "Canis familiaris"

#     # Constructor method (initializer)
#     def __init__(self, name, age):
#         # Instance variables
#         self.name = name
#         self.age = age

#     # Instance method
#     def bark(self):
#         print("Woof!")

#     # Another instance method
#     def describe(self):
#         print(f"{self.name} is {self.age} years old.")

# # Creating instances of the Dog class
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 5)

# # Accessing attributes and calling methods
# print(dog1.name)  # Output: Buddy
# print(dog2.age)   # Output: 5

# dog1.bark()       # Output: Woof!
# dog2.describe()   # Output: Max is 5 years old.


def find_max_and_positions(arr):
    def flatten_recursive(lst, prefix=[]):
        result = []
        for i, el in enumerate(lst):
            if isinstance(el, list):
                result.extend(flatten_recursive(el, prefix + [i]))
            else:
                result.append((prefix + [i], el))
        return result

    # Flatten the nested array
    flattened = flatten_recursive(arr)

    # Initialize variables to store the maximum element and its positions
    max_element = flattened[0][1]  # Assume the first element is the maximum initially
    max_positions = [flattened[0][0]]  # Initialize with the position of the first element

    # Iterate through the flattened array to find the maximum element and its positions
    for i in range(1, len(flattened)):
        indices, element = flattened[i]
        if element > max_element:
            max_element = element
            max_positions = [indices]
        elif element == max_element:
            max_positions.append(indices)

    return max_element, max_positions

# Example usage
array = [3, 58, 58, 21, [3, 58, 58, 21,[4, 58],58], [3, 58]]
max_value, max_indices = find_max_and_positions(array)

# Print the result
print("The maximum element(s) in the array is/are:", max_value)
print("The index/indices of the maximum element(s) is/are:", max_indices)