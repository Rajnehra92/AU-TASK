N1=int(input("Enter a number:"))
N2=int(input("Enter a number:"))
sum=N1+N2
print(sum)


#Task
#Q1:- Write a program that will convert celsius value to fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")

# Q2:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
def swap_to_numbers(num1,num2):
    temp=num1
    num1=num2
    num2=temp
    return swap_to_numbers

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
print("After swapping:",num2,num1)


# Q3:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.
import math
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
print("Enter the coordinates of the first point (x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Enter the coordinates of the second point (x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
distance = calculate_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between the points is: {distance:.2f}")


#Q4:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
def calculate_simple_interest(principal,rate_of_interest,time_period):
    simple_interest=(principal*rate_of_interest*time_period)/100
    return simple_interest
principal=float(input("Enter value of principal:"))
rate_of_interest=float(input("Enter value of rate_of_interest:"))
time_period=float(input("Enter value of time_period:"))
simple_interest=calculate_simple_interest(principal,rate_of_interest,time_period)
print(f"The simple interest of:",simple_interest)

#Q.5:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
#For example:
#   Input:
#       heads -> 4
#       legs -> 12
#   Output:
#       dogs -> 2
#       chicken -> 2
total_heads = int(input("Enter the total number of heads: "))
total_legs = int(input("Enter the total number of legs: "))
chickens = (4 * total_heads - total_legs) // 2
dogs = total_heads - chickens
if chickens < 0 or dogs < 0 or 2 * chickens + 4 * dogs != total_legs:
    print("No valid solution exists with the given heads and legs.")
else:
    print(f"Number of chickens: {chickens}")
    print(f"Number of dogs: {dogs}")
    
# Q.6:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
n = int(input("Enter the value of n: "))
sum_of_squares = 0
for i in range(1, n + 1):
    sum_of_squares += i ** 2
print("The sum of squares of first", n, "natural numbers is:", sum_of_squares)

#Q.7:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
# Get inputs from the user
a1 = int(input("Enter the first term: "))
a2 = int(input("Enter the second term: "))
n = int(input("Enter the term number to find: "))
d = a2 - a1
an = a1 + (n - 1) * d
print(f"The {n}th term of the arithmetic series is: {an}")

#Q.8:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
def sum_of_fractions(a,b,c,d):
  sum_of_fractions = ((a*b)+(c*d))/(b*d)
  return sum_of_fractions
a=int(input("Enter the numerator of the first fraction: "))
b=int(input("Enter the denominator of the second fraction: "))
c=int(input("Enter the numerator of the third fraction: "))
d=int(input("Enter the denominator of the forth fraction: "))
sum = sum_of_fractions(a,b,c,d)
print("The sum of the fractions is:",sum)


# Q.9:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
#Input:
#Dimensions of the milk tank<br>
#H = 20cm, L = 20cm, B = 20cm
#Dimensions of the glass<br>
#h = 3cm, r = 1cm
# Get inputs from the user
height = float(input("Enter the height of the milk tank (cm): "))
width = float(input("Enter the width of the milk tank (cm): "))
breadth = float(input("Enter the breadth of the milk tank (cm): "))
glass_volume = 250 
tank_volume = height * width * breadth
number_of_glasses = tank_volume // glass_volume 
print(f"The number of full glasses of milk that can be obtained is: {int(number_of_glasses)}")

#Task
#Problem10: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) 
#and taxes deduction as below:
#Salary(Lakhs) : Tax(%)
#Below 5 : 0%
#5-10 : 10%
#10-20 : 20%
#aboove 20 : 30%**bold text**
def final_Salary(Salary):
  HRA = 0.10*Salary
  DA = 0.05*Salary
  PF = 0.03*Salary
  if Salary<=5000:
    print("Tax deduction 0%")
  elif Salary<=10000:
    print("Tax deduction 10%")
  elif Salary<=20000:
    print("Tax deduction 20%")
  else:
    print("Salary is not correct")
  final = Salary - (HRA+DA+PF)
  return final
print(final_Salary(15000) )

#Problem12: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
a = int(input("Enter a angle"))
b = int(input("Enter a angle"))
c = int(input("Enter a angle"))
if a+b+c == 180:
  print("It is a triangle")
else:
  print("It is not a triangle")


#Problem 13: Write a program that will take user input of cost price and selling price 
#and determines whether its a loss or a profit.
cost_price = float(input("Enter a cost price"))
selling_price = float(input("Enter a selling price"))
if cost_price>selling_price:
  print("It is a loss of",cost_price-selling_price)
elif cost_price<selling_price:
  print("It is a profit of",selling_price-cost_price)
else:
  print("It is a loss")


#Problem 14: Write a menu-driven program -
#1. cm to ft
#2. km to miles
#3. USD to INR
#4. exit
def convert(n):
  ft=n/30.48
  miles=n/1.609
  INR=n/84.40
  return ft,miles,INR
n=int(input("Enter a number:"))
ft, miles, INR = convert(n)
print("value of {n}cm to {ft}ft:",ft)
print("value of {n}km to {miles}miles:",miles)
print("value of {n}usd to {INR}INR:",INR)
print("Exit")


#Problem 15: Display Fibonacci series up to 10 terms.
#Note: The Fibonacci Sequence is a series of numbers. 
#The next number is found by adding up the two numbers before it. 
#The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. 
#The next number in this series above is 13+21 = 34
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n+1):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(5))


#Problem 16: Find the factorial of a given number.
#Write a program to use the loop to find the factorial of a given number.
#The factorial (symbol: `!`) means to multiply all whole numbers from the chosen number down to 1.
#For example: calculate the factorial of 5
#5! = 5 × 4 × 3 × 2 × 1 = 120
Output:120
n = int(input("Enter a number"))
fact = 1
for i in range(1, n + 1):
    fact = fact*i
print(fact)


#Problem 17:Reverse a given integer number.
#Example:
#Input:76542
#Output:24567
N = int(input("Enter a number"))
while N > 0:
    last_digit = N % 10
    print(last_digit, end="")
    N = N // 10

#Problem 18: Take a user input as integer N. Find out the sum from 1 to N.
# If any number if divisible by 5, then skip that number. And if the sum is greater than 300, 
#don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.
#Example1:
#Input:30
#Output:276
N = int(input("Enter a number: "))
i = 1
sum = 0
while i <= N and sum <= 300:
    if i % 5 != 0:
        sum = sum + i
    i = i+1
print("Final sum:", sum)

#Problem 19: Write a program that keeps on accepting a number from the user until the user enters Zero.
#Display the sum and average of all the numbers.
a = int(input("Enter a number"))
sum=0
temp = a
for a in range(a,0,-1):
  sum =sum+a
  Average=sum/temp
  print(a)
print(sum)
print(Average)

#Problem 20: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
for i in range(2000,3201):
  if(i%7==0 and i%5!=0):
    print(i,end=",")

#Problem 21: Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number. 
# The numbers obtained should be printed in a space-separated sequence on a single line.
for i in range(1000,3000):
  N=i
  flag=True
  while N>0:
    last_digit=N%10
    if last_digit%2 != 0:
      flag=False
      break
    N=N//10
    if flag:5
    print(i,end=" ")


#Problem 22: A robot moves in a plane starting from the original point (0,0). 
#The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
#The trace of robot movement is shown as the following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#The numbers after the direction are steps.
#means robot stop there.
#Please write a program to compute the distance from current position after a sequence of movement and original point.**
#If the distance is a float, then just print the nearest integer.*
#Example:
#Input:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#Output:2
x=0
y=0
print("up",1)
print("down",2)
print("left",3)
print("right",4)
a1 = int(input("Enter a number:"))
a2 = int(input("Enter a number:"))
if (a1== 1):
    a2=y+a2
    print("for move up:",a2)
elif (a1 == 2):
    a2=y-a2
    print("for move down:",a2)
elif (a1 == 3):
    a2=y+a2
    print("for move left",a2)
elif (a1 == 4):
    a2=y-a2
    print("for move right",a2)
else:
    print(exit)
    
#Problem 23:Write a program to print whether a given number is a prime number or not
n = int(input("Enter a number"))
if n==1 or n==0:
  print("not a prime number")
if n>1:
  for i in range(2,n):
    if(n%i)==0:
      print("not a prime number")
      break
  else:
    print("a prime number")


#Problem 24:Print all the Armstrong numbers in a given range.
#Range will be provided by the user
#Armstrong number is a number that is equal to the sum of cubes of its digits. 
#For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
number=int(input("Enter a number"))
def armstrong(number):
  digits=str(number)
  power=len(digits)
  total=sum(int(digit)**power for digit in digits)
  return total
if number==armstrong(number):
  print("Armstrong number")
else:
  print("Not armstrong number")

#Problem 25:Calculate the angle between the hour hand and minute hand.
#Note: There can be two angles between hands; we need to print a minimum of two. 
#Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.
#Input:H = 9 , M = 0
#Output:90
#Explanation:The minimum angle between hour and minute hand when the time is 9 is 90 degress.
def clock_angle(H,M):
  clock_angle= abs((11/2)*M-30*H)
  return clock_angle
H = int(input("Enter value of hour"))
M = int(input("Enter value of minute"))
angle=360-clock_angle(H,M)
print(angle)


#Problem 26:Given two rectangles,
#find if the given two rectangles overlap or not.
#A rectangle is denoted by providing the x and y coordinates of two points: 
#the left top corner and the right bottom corner of the rectangle. 
#Two rectangles sharing a side are considered overlapping. 
#(L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).
x1=int(input(" "))
y1=int(input(" "))
x2=int(input(" "))
y2=int(input(" "))
x3=int(input(" "))
y3=int(input(" "))
x4=int(input(" "))
y4=int(input(" "))
def do_overlap(x1,y1,x2,y2,x3,y3,x4,y4):
  if x2<=x3 or x4<=x1:
    return False
  if y2>=y3 or y4>=y1:
    return False
  return True
if do_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
  print("do overlap")
else:
  print("do not overlap")

