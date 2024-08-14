numbers = [1, -2, 3, 4, -5, 6]
sum = 0
for i in range(len(numbers)):
    if numbers[i] > 0:
        sum += numbers[i]
print(sum)
