height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / pow(height, 2)

if height > 3:
    raise ValueError("Invalid Height! Human height should not be over 3 meters")

print(bmi)