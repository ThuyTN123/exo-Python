A = [10, 22, 64, 20, 1]
total = 0

# Calculate the total using a for loop
for i in A:
    total += i

# Output the result
print(f"The total of the elements of array A is: {total}")


B = [10, 22, 64, 20, 1]
sum = 0

# Calculate the total using a for loop with len() and range()
for i in range(len(B)):
    sum += B[i]

# Output the result
print("The total of the elements of array B is:", sum)