# User inputs the original weight value, which must be a float:
weight1 = 0  # variable needs defining before the loop
while True:
    try:
        weight1 = float((input("Enter the weight number: ")))
    except ValueError:
        print("Invalid weight input. Please try again.")
        continue
    else:
        break

# User inputs the unit of this weight, which must be either kg, st, lbs, oz:
unit1 = input("Enter the unit of this weight (kg, st, lbs, oz): ")
while unit1 not in ["kg", "st", "lbs", "oz"]:
    print("Invalid unit input. Please try again.")
    unit1 = input("What is the unit of this weight (kg, st, lbs, oz): ")

# User inputs the unit that he/she wants to covert their original weight to:
unit2 = input("What you would like this converting to (kg, st, lbs, oz): ")
while unit2 not in ["kg", "st", "lbs", "oz"]:
    print("Invalid unit input. Please try again.")
    unit2 = input("Enter the unit of this weight (kg, st, lbs, oz): ")

# Conversion calculations
if unit1 == unit2:
    weight2 = weight1
    print(f"{weight1}{unit1} is equal {weight2}{unit2}.")
elif unit1 == "kg" and unit2 == "st":
    weight2 = round(weight1 / 6.35, 1)
    print(f"{weight1}{unit1} is equal {weight2}{unit2}.")
elif unit1 == "kg" and unit2 == "lbs":
    weight2 = round(weight1 * 2.205, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "kg" and unit2 == "oz":
    weight2 = round(weight1 * 35.274, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "st" and unit2 == "kg":
    weight2 = round(weight1 * 6.35, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "st" and unit2 == "lbs":
    weight2 = round(weight1 * 14, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "st" and unit2 == "oz":
    weight2 = round(weight1 * 224, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "lbs" and unit2 == "kg":
    weight2 = round(weight1 / 2.205, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "lbs" and unit2 == "st":
    weight2 = round(weight1 / 14, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "lbs" and unit2 == "oz":
    weight2 = round(weight1 * 16, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "oz" and unit2 == "kg":
    weight2 = round(weight1 / 35.274, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "oz" and unit2 == "st":
    weight2 = round(weight1 / 224, 2)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")
elif unit1 == "oz" and unit2 == "lbs":
    weight2 = round(weight1 / 16, 1)
    print(f"{weight1}{unit1} is equal to {weight2}{unit2}.")