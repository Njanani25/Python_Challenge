arr = [3, 1, 7, 2, 9, 5]
max_element = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
print("The maximum element in the array is:", max_element)
