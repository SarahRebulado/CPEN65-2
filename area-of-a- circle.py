import math


def Area(radius):
    area = (math.pi * radius * radius)
    return area


def Area1(diameter):
    area1 = (math.pi * diameter * diameter)/4
    return area1


while True:

    choice = input(" Enter 1 to get Area using radius \n Enter 2 to get Area using diameter \n Exit type 3 \n")
    if choice == '1':
        print("Solving area of the circle given radius")
        radius = float(input("Enter radius:"))
        print("Area of the circle is (units squared): %.2f" % Area(radius))
    elif choice == '2':
        print("Solving area of the circle given diameter")
        diameter = float(input("Enter diameter:"))
        print("Area of the circle is (units squared) : %.2f" % Area1(diameter))
    if choice == '3':
        break
