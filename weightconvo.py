

weight = int(input("Enter your weight: "))
unit = input("Enter the unit (kg or lb): ").lower()


if unit == "kg":
  converted = weight * 0.45
  print(f"Your weight is {converted} lb")
else:
  converted = weight / 0.45
  print(f"Your weight is {converted} kg")
