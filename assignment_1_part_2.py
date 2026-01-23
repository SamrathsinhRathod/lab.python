Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
radius=float(input("Enter the radius of The circle:"))
Enter the radius of The circle:5
area=3.14*radius*radius
circumference=2*3.14*radius
print("Area of the circle:",area)
Area of the circle: 78.5
print("circumference of the circle",circumference)
circumference of the circle 31.400000000000002
principal=float(input("Enter the principal amount:"))
Enter the principal amount:5000
rate=float(input("Enter the annual interest rate(in%):"))
Enter the annual interest rate(in%):5
time=float(input("Enter the time (in years):"))
Enter the time (in years):9
simple_interest=(principal*rate*time)/100
print(f"\nresults:")

results:
50000
50000
print(f"principal:",principal)
principal: 5000.0
print(f"interest rate:",rate)
interest rate: 5.0
print(f"the simple ineterst is:",simple_interest)
the simple ineterst is: 2250.0
legth=10
width=5
print(2*(length+width))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(2*(length+width))
NameError: name 'length' is not defined. Did you mean: 'legth'?
length=10
width=5
print(2*(length+width))
30
l=10
w=5
print("perimeter:",2*(l+w))
perimeter: 30
print("Area:",l*w)
Area: 50
a=5
b=6
c=7
print("perimeter:",a+b+c)
perimeter: 18
s=float(input())
s=float(input("Enter side:"))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s=float(input())
ValueError: could not convert string to float: 's=float(input("Enter side:"))'
s=float(input("Enter side:"))
Enter side:4
print("Area:",s*s)
Area: 16.0
print("perimeter:",4*s)
perimeter: 16.0
side=float(input("Enter the side length:"))
Enter the side length:4*side
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    side=float(input("Enter the side length:"))
ValueError: could not convert string to float: '4*side'
side=float(input("Enter the side length:"))
Enter the side length:5
perimeter=4*side
print("the perimeter is:",perimeter)
the perimeter is: 20.0
\
