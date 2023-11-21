
# arrayA = [3, 58, 11, 21]
# max_A = max(arrayA)
# print("The maximum element in the arrayA is:", max_A)

arrayB = [3, 58, 11, 21]
max_B = arrayB[0] 
for i in arrayB:
    if i > max_B:
        max_B = i
print("The maximum element in the arrayC is:", max_B)



arrayC = [3, 58, 11, 21]
max_C = arrayC[0] 

for j in range(len(arrayC)):
    if arrayC[j] > max_C:
        max_C = arrayC[j]
print("The maximum element in the arrayB is:", max_C)


arrayD = [3, 58, 58, 21]
max_D = arrayD[0] 
max_pD = [0]  

for e in range(1, len(arrayD)):
    arraymax = arrayD[e]
    if arraymax > max_D:
        max_D = arraymax
        max_pD = [e]
    elif arraymax == max_D:
        # max_pD.append(e); to add value in the list
        max_pD = max_pD + [e] # the other way to add value in the list
        
print("The maximum element(s) in the arrayD is/are:", max_D)
print("The position(s) of the maximum element(s) in arrayD is/are:", max_pD)

