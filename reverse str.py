string = input("Enter a string: ")
reverse_string = " ".join(word[::-1] for word in string.split())
print("reversed string is",reverse_string)
