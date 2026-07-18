# Find Second Smallest Element

numbers = [12, 45, 7, 89, 23]

smallest = float('inf')
second_smallest = float('inf')

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif smallest < num < second_smallest:
        second_smallest = num

print("Smallest:", smallest)
print("Second Smallest:", second_smallest)
