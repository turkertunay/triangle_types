a = int(input("enter the first side of the triangle: "))
b = int(input("enter the second side of the triangle: "))
c = int(input("enter the third side of the triangle: "))

sum_a_b = a+b
dif_a_b = abs(a-b)

if sum_a_b >= c and dif_a_b <= c:
    print("this triangle can exist.")
    if a != b and a != c and b != c:
        print("this triangle is a scalene triangle")
    elif a == b and a == c and b == c:
        print("this triangle is an equilateral triangle")
    else:
        print("this triangle is an isosceles triangle")
else:
    print("this triangle can  not exist.")

