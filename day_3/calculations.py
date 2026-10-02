age = int(19)
height = float(input("Enter your height in meters: "))
width = float(input("Enter your width in meters: "))

area = height * width

print(f"The area is: {area} square meters")

if area > 25:
    print("The area is greater than 25 square meters.")
else:
    print("The area is too small.")

