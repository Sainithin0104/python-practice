numbers = [12, 45, 8, 99, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element is:", largest)
