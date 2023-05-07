string = input("Enter a string: ")
substring = input("Enter a substring to check: ")
if string.startswith(substring):
    print("it starts with given substring.")
else:
    print("does not start with given substring.")
