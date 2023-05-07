print("Welcome To Python Calculator :)")
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = str(input("Enter Operation Symbol (ex:+,-,*,/) :"))

if c == "+":
    print(f"The Addition of {a} and {b} is", a + b)
elif c == "-":
    print(f"The Subtraction of {a} and {b} is", a - b)
elif c == "*":
    print(f"The Multiplication of {a} and {b} is", a * b)
elif c == "/":
    print(f"The Division of {a} and {b} is", a / b)
elif c == "//":
    print(f"The Division of {a} and {b} is", a // b)
elif c == "%":
    print(f"The Modulus of {a} and {b} is", a % b)
elif c == "^":
    print(f"{a} Power {b} is", a ^ b)
else:
    print("enter valid operator!")
# try to add 1.Try Again to run program again And 2. For Exit O_o
d = int(input("Press 1 For Try Again Or 2 To Exit: "))
if d==1:
    print()
else:
    print("Thank You")
#incomplete