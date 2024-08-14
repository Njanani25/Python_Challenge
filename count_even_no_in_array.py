arr = [3, 1, 7, 2, 9, 5, 8, 4]
even_count = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even_count += 1
print("The number of even numbers in the array is:", even_count)
