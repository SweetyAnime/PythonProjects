student = int(input("Enter Student Total Mark(Out Of 100) :"))
if student<=50:
    print("Fail")
elif student>50 and student<=60:
    print("Good")
elif student>60 and student<=80:
    print("Very Good")
elif student>80 and student<=100:
    print("Outstanding")
else:
    print("Student Mark Should Be Above 0 and Below 100")