n = int(input("Enter total numbers in list: "))
numbers = [int(input("Enter element: "))
           for i in range(n)]
largest = max(numbers)
smallest = min(numbers)
print("The largest number is",largest)
print("The smallest number is",smallest)