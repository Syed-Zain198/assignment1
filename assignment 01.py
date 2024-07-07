# Write your code here
name = 'zain'
father_name = 'akram'
date_of_birth = '01-07-2003'
print(f'my name is : {name} , my father_name is : {father_name} , my date of birth is : {date_of_birth}')


#2. Write your small bio using variables and print it using print function

name = 'zain' #string
print(name)
print(type(name))
age = 21 #integer
print(age)
print(type(age))
weight = 75 #float
print(weight)
print(type(weight))
male = True #boolean
print(male)
print(type(male))


#3. Write a program in which use all the operators we can use in Python


a = 5
b = 4
print('adition:', a+b)
print('subtraction:', a-b)
print('multiply:', a*b)
print('divide:', a/b)
print('power:', a**b)
print('floor:', a//b) #round off lower



import math #round off uper
a = 14/3
b = (math.ceil(a))
print('result is :', b)


a = 93/7
b = (math.ceil(a))
print('result is :' , b)



#4. Completes the following steps of small task:
    #- Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
    #- Mention Variable of Total Marks and assign 300 to it
    #- Calculate Percentage


English = 70
Islamiat = 80
Math = 90
total_marks = 300
total_marks_obtained = English + Islamiat + Math
print(f'Total marks is : {total_marks}')
print(f'Total marks obtained is : {total_marks_obtained}')
print('percentage is:' , total_marks_obtained/total_marks*100)



# Part -2 Python Basics (Conditional Statements)


#1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.


years_of_service = 5
salary=int(input('what is your salary: '))
years_of_service=int(input('year of service: '))

if years_of_service > 5 :
    bonus = salary*0.05 
else:
    bonus = 0

print('Net bonus amount is : ' , salary*0.05)



#2) Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible


int(input('enter your age : '))
if age > 17:
    print('you are eligible fot voting')
else:
    print('you are not eligible')


 #   3) Write a program to check whether a number entered by user is even or odd.



number = int(input('enter your number: '))
if number % 6 == 0 :
    print(f'entered {number} is even')
else:
    print(f'entered {number} is odd')



    
    #4) Write a program to check whether a number is divisible by 7 or not.
#Show Answer



number = int(input('enter your number'))
if number % 7 == 0 :
    print(f'{number} is divisible by 7')
else:
    print(f'{number} is not divisible by 7')




    #5) Write a program to display 
#"Hello" if a number entered by user is a multiple of five , otherwise print "Bye".



number = int(input('enter your number'))
if number % 5 == 0:
    print('hello')
else:
    print('bye')



#7) Write a program to display the last digit of a number.  


number = int(input('enter your number'))
last_digit = number % 10
print('last digit of number is : ' , last_digit)



#9) Take values of length and breadth of a rectangle from user and print if it is square or rectangle.



Length = int(input('value of length is : '))
Breadth = int(input('value of breadth is : '))
if Length == Breadth:
    print('This is Square')
else:
    print('This is Rectangle')


    
    
#10) Take two int values from user and print greatest among them.



value_1 = int(input('enter your value'))
value_2 = int(input('enter your value'))
if value_1 > value_2 :
    print(f'the gratest value is value 1 {value_1}')
else:
    print(f'the gratest value is value 2 {value_2}')



 #   11) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.




quantity = int(input('Enter the quantity of items: '))
total_cost = quantity * 100
if total_cost >= 1000:
    discount = total_cost * 0.1
    total_cost -= discount
    print('total cost of user is: ' , {total_cost} )
else:
    print('No discount for user')




 #   12) A school has following rules for grading system:

#. 25 to 45 - E

#c. 45 to 50 - D

#d. 50 to 60 - C

#e. 60 to 80 - B

#f. Above 80 - A

#Ask user to enter marks and print the corresponding grade.


marks = int(input('Enter your marks: '))

if marks < 25:
    print('your grade is F')
elif 25 <= marks <= 45:
    print('your grade is E')
elif 45 < marks <= 50:
    print('your grade is D')
elif 50 < marks <= 60:
    print('your grade is C')
elif 60 < marks <= 80:
    print('your grade is B')
else:
    print('your grade is A')



#14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.

#Take following input from user

#- Number of classes held

#- Number of classes attended.

#And print

#- Is student is allowed to sit in exam or not.


number_of_classes = int(input('Enter number of classes held : '))
number_of_classes_attended = int(input('Enter number of classes attended : '))
attendence = number_of_classes_attended / number_of_classes * 100
if attendence >= 75:
    print(F'student is allowed to sit in exam and his percentage of class attended is : {attendence}%' )
else:
    print(F'student is not allowed to sit in exam and his percentage of class attended is : {attendence}%' )




 #   15) Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.



medical_cause = input('Do you have medical cause : ')
if medical_cause == 'NO':
    print('student is allowed to sit in exam')
else:
    print('student is not allowed to sit in exam')






 #If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.






def  is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")





    #if employee is a male and age is in between 20 to 40 then he may work in anywhere

#ny other input of age should print "ERROR"



employee_gender = input('enter employee gender : ')
employee_age = int(input('enter employee age : '))
employee_martial_status = input('enter employee martial status : ')
if employee_gender == 'F':
    print('employee will work only in urban areas')
elif(employee_gender == 'M') and (25<= employee_age <=40):
    print('employee is male and will work any where')
elif (employee_gender == 'M') and (40<= employee_age <=60):
    print('employee is male and will work in urban areas only')
else:
    print('ERROR')






    #6) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
     #Unit                                                     Price  
#uptp 100 units                                             no charge
#Next 200 units                                              Rs 5 per unit
#(For example if input unit is 97 than total bill amount is Rs.0
#(For example if input unit is 150 than total bill amount is Rs.750
 

 units = int(input("Enter the number of units: "))
total_bill = 0
if units <= 100:
    total_bill = 0
elif units <= 300:
    total_bill = (units - 100) * 5
elif units > 300:
    total_bill = 200 * 5 + (units - 300) * 10
print(f"The total bill amount is Rs. {total_bill}")






#13) Take input of age of 3 people by user and determine oldest and youngest among them.



ali_age = int(input('enter ali age :'))
atif_age = int(input('enter atif age :'))
amin_age = int(input('enter amin age :'))
oldest = max(ali_age, atif_age, amin_age)
youngest = min(ali_age, atif_age, amin_age)
print(f"The youngest person is {youngest} years old.")
print(f"The oldest person is {oldest} years old.")










