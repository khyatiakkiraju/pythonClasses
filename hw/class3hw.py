#PERCENTAGE CALCULATOR
math=int(input("What did you get on math?"))
english=int(input("What did you get on english?"))
history=int(input("What did you get on history?"))
spanish=int(input("What did you get on spanish?"))
science=int(input("What did you get on science?"))
total = print(math+english+history+spanish+science)
percentage = print(math+english+history+spanish+science / 100)

#Simple Interest
principal = int(input("a number for principal: "))
rate = int(input("a number for rate: "))
time = int(input("a number for time: "))
simpleInterest = int(print(principal*rate*time))

#Temperature Converter
tempC = int(input("what is the temperature in celcius?"))
tempF = int(print((tempC * 9/5)+32))

#Square and Cube
num = int(input("a number: "))
square = int(print(num**2))
cube = int(print(num**3))

#Average of 4 Numbers
num1 = int(input("Give Num: "))
num2 = int(input("Give Num: "))
num3 = int(input("Give Num: "))
num4 = int(input("Give Num: "))
average = int(print(num1 + num2 + num3+ num4 / 4))

#Marks Formatter
name = input("What is your name?")
grade = input("what grade are you in?")
score1 = int(input("what did you get in one of your classes?"))             
score2 = int(input("what did you get in another one of your classes?"))  
score3 = int(input("what did you get in another one of your classes?"))        
averageScore = print(score1+score2+score3 / 3)