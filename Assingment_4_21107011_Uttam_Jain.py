import random

#Question No.1 

print("QUESTION No.1:")

#entering the number of marks by the user
marks=float(input("enter the number of marks: "))
#converting it into grades
if marks>=80 :
    print("Grade of the student : A\n")
elif 60<=marks<80 :
    print("Grade of the student : B\n")
elif 50<=marks<60 :
    print("Grade of the student : C\n")
elif 45<=marks<50 :
    print("Grade of the student : D\n")
elif 25<=marks<45 :
    print("Grade of the student : E\n")
else :
    print("Grade of the student : F\n")
    
#Question No.2 

print("QUESTION No.2:")  
  
#entering the year 
year=int(input("enter the year: "))
#checking if it is leap year or not
if year%4 == 0 and year%100 == 0:
        if year%400 == 0:
            print("It is a leap year\n")
        else :
            print("not a leap year\n")
elif year%4 == 0:
    print("It is a leap year\n")
else :
    print("not a leap year\n")
    
#Question No.3 

print("QUESTION No.3:") 
  
#10 randomly generated questions
for x in range(10):
#2 randomly generated numbers
    random1 = random.randint(0,10)
    random2 = random.randint(0,22)
    print("Question ",x+1,": ",random1," x ",random2)
#user entering his answer
    user_answer = int(input())
    answer = random1*random2
    if user_answer == answer:
        print("Right!\n")
    else :
        print("Wrong. The answer is ",answer,"\n")
       
#Question No.4 

print("QUESTION No.4:")   

#program to determine how many pieces are in the bowl
for x in range(200):
    if x%5 == 2:
      if x%6 == 3:
        if x%7 == 2:
         print("There are ",x," candies in the jar")

    