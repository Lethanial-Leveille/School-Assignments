side_length_1 = float(input("Side length 1: "))
side_length_2 = float(input("Side length 2: "))
side_length_3 = float(input("Side length 3: "))

if side_length_1 == side_length_2:
    if side_length_1 == side_length_3:
        print("This is an equilateral triangle!")
    else:
        print("This is an isosceles triangle!")
elif side_length_1 == side_length_3:
    print("This is an isosceles triangle!")
else:
    print("This is a scalene triangle!")