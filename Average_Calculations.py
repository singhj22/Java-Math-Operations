'''
Created on Sep 25, 2018

@author: Jugat Singh
Operations Practice
'''

print("Welcome to the test score calculator.")
print("\n\n\n\n")

# input the test sores
test1= float(input("Please enter the first test score: "))
test2= float(input("Please enter the second test score: "))
test3= float(input("Please enter the third test score: "))

# calculate the average
average= (test1 + test2 + test3) / 3
print("\n")

# Display the output
print("Average Test Score: ", average)
print("\n\n")

#Slope Calculator
input("Press enter to calculate a slope")

print("Welcome to the slope calculator")

#Define variables
y2=float(input("Enter the value of Y2: "))
y1=float(input("Enter the value of Y1: "))
x2=float(input("Enter the value of X2: "))
x1=float(input("Enter the value of X1: "))

#Calculate Slope

Dy= y2-y1
Dx= x2-x1

#Display the output
print(Dy, "/", Dx)

#Tax

input("press enter to calculate tax for PA")

price= float(input("Please input the price: "))

tax= price*.06

total= price+ tax

print("the tax is $", tax, "the total is $", total) 

