#converts weight from kg to lbs and viceversa
weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    weightKg = int(weight) / 0.45
    print(f"you are {weightKg} kilos")
elif unit.upper() == "K":
    weightLbs = int(weight) * 0.45
    print(f"you are {weightLbs} pounds")
else:
    print("enter a unit of measurement")
