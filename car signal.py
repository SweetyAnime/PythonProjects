a = input("Enter Signal Colour :")
car = a.lower()
if car=="green":
    print("Car Is Allowed To Go")
elif car=="yellow":
    print("Car Has to wait")
elif car=="red":
    print("car has to stop")
else:
    print("Enter valid colour")