student = int(input("Enter Student Total Mark(Out Of 500) :"))
if student<=100:
    print("Satisfactory")
elif student<=200:
    print("Good")
elif student<=300:
    print("Very Good")
elif student<=400:
    print("Excellent")
elif student<=500:
    print("Outstanding")
else:
    print("Enter Valid Mark")