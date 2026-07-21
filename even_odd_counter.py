numbers = []

even = 0
odd = 0

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("\nEntered Numbers:", numbers)
print("Even Numbers :", even)
print("Odd Numbers  :", odd)
