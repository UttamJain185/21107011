# -*- coding: utf-8 -*-
"""
Created on Thu May 12 22:10:20 2022

@author: administrator
"""

import math
import cmath

#QUESTION NO.1

print("QUESTION NO.1")

#converting a number into its binary equivalent
Number=int(input("Enter a number: "))
Num_bin=[]
while(Number>0):
    Bin_digit=Number%2
    Num_bin.append(Bin_digit)
    Number=Number//2
Num_bin.reverse()
print("Binary Equivalent is: ")
for i in Num_bin:
    print(i,end=" ")
    
print("\n")    

#QUESTION NO.2

print("QUESTION NO.2")

#entering the first number by user
num_1 = float(input("enter your 1st number: "))
#user entering his choice of operator
operator = input("enter your operator : ")
#entering the secound number by user
num_2 = float(input("enter your 2nd number : "))

if(operator == '+'):
    result = num_1+num_2
elif(operator == '-'):
    result = num_1 - num_2
elif(operator == '*'):
    result = num_1*num_2
elif(operator == '/'):
    result = num_1/num_2
else:
    result="invalid operator"

#printing the value of expression 
print(num_1,operator,num_2," = ",result,"\n")

#QUESTION NO.3

print("QUESTION NO.3(a)")
print("result of the expression : ",(3+4)*5,"\n")

print("QUESTION NO.3(b)")
n = float(input("Enter your value of n: "))
print("result of the expression : ",n*(n-1)/2,"\n")

print("QUESTION NO.3(c)")
r = float(input("Enter your value of r: "))
result=4*math.pi*r*r
print("result of the expression : ",round(result,2),"\n")

print("QUESTION NO.3(d)")
r=float(input("Enter your value of r: "))
a=float(input("Enter your value of a: "))
b=float(input("Enter your value of b: "))
num = r*math.cos(a)**2 
num1 = r*math.sin(b)**2
#printing the value of given expression
print("result of the expression : ",math.sqrt(num + num1),"\n")

print("QUESTION N0.3(e)")
x1=float(input("Enter your value of x1: "))
x2=float(input("Enter your value of x2: "))
y1=float(input("Enter your value of y1: "))
y2=float(input("Enter your value of y2: "))
a=y2-y1
b=x2-x1
print("result of the expression : ",a/b,"\n")



#QUESTION NO.4
#printing different ranges

print("QUESTION N0.4(a)")
for i in range(5):
    print(i)
    print("")
    
print("QUESTION N0.4(b)")    
for i in range(3,10):
    print(i)
    print("")

print("QUESTION N0.4(c)")
for i in range(4,13,3):
    print(i)
    print("")

print("QUESTION N0.4(d)")
for i in range(15,5,-2):
    print(i)
    print("")

print("QUESTION N0.4(e)")
for i in range(5,3):
    print(i)
    print("")
    
print("\n")    

#QUESTION NO.5

print("QUESTION NO.5")
#number of hydrogen atoms
num_h=int(input("Enter number of hydrogen atoms : \n"))
#number of carbon atoms
num_c=int(input("Enter number of Carbon atoms : \n"))
#number of oxygen atoms
num_o=int(input("Enter number of Oxygen atoms : \n"))

Mass_C=12.0107
Mass_H=1.00794
Mass_O=15.9994
#calculating the mass of molecule
Mass_Molecule=(num_h*Mass_H)+ (num_c*Mass_C)+(num_o*Mass_O)
#printing the mass of molecule
print("The mass of molecule = ",Mass_Molecule)





