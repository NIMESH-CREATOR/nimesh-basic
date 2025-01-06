for number in range(1,101):

  if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#wap 

num = int(input("enter the number: "))    

if num%2 == 0:
   print(num,"is even number")
else:
   print(num,"is odd number")  


# find 

import math

rad = float(input("enter the radius of the circle: "))

area = math.pi * rad * rad

print(f"the area of circle is: {area:.2f}")

#second pro

r = float(input("enter the numb: "))
pi = 3.14
area = pi * r * r
print(area,"circle of area ")