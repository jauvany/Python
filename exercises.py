#01
Exponentiation


Write code to output 4 raised to the 5th power.
Output the result using the print() statement.

#your code goes here
print(4**5)

Flight Time

#02
You need to calculate the flight time of an upcoming trip. You are flying from LA to Sydney, covering a distance of 7425 miles, the plane flies at an average speed of 550 miles an hour.

Calculate and output the total flight time in hours.

Hint
The result should be a float.
Use the print statement to output the result.

"""Solution """
print(7425 / 550)


#03
Strings


You are given a code that should output a string with quotes.
However, it contains errors.
print('I'm learning Python. It's easy.')

Task
Fix the given code to generate the expected output.
Remember, you need to escape the quotes in the strings to fix the errors in the code.

"""Solution"""

print('I\'m learning Python. It\'s easy.')

#04
Strings


Write a program to output the letters A B C D, each on a separate line.
You can use 3 quotes to add the new lines.

"""solution"""

print('''A
B
C
D''')

#05
String Operations


You’re given a task to write the word "hi" 42 times. Boring, right?

Write a program to do it for you.

Create a program to output "hi" 42 times, without any separators, on the same line.
Remember, you can multiply strings by numbers.

"""Solution"""
#your code goes here
print("hi" * 42)

#06

Input


Somebody wrote code to take a string input and output it, repeated 10 times.
However, the code results in an error.
Fix the code to output the desired output.

x = input()

print(x+10)

"""Solution"""

#07

Problem
Working with Input

#08
Problem
else Statement


Write a program to control entrance to a club.
Only people who are 18 or older are allowed to enter the club.
Your program takes the age of the person who tries to enter, and outputs "Allowed" if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.

Sample Input
24

Sample Output
Allowed

""" Solution """

age = int(input())
if age >= 18:
    print("Allowed")
else:
    print("Sorry")

    


Write a program to take x and y as input and output the string x, repeated y times.

Sample Input
hi
3

Sample Output
hihihi
Remember to convert the input to the required data type.

"""Solution"""

x = input()
y = input()

print(str(x) * int(y))

#08
spam = "7"
spam = spam + "0"
eggs = int(spam) + 3
print(float(eggs))

Answer = 73.0

#09

Tip Calculator


When you go out to eat, you always tip 20% of the bill amount. But who’s got the time to calculate the right tip amount every time? Not you that’s for sure! You’re making a program to calculate tips and save some time.

Your program needs to take the bill amount as input and output the tip as a float.

Sample Input
50

Sample Output
10.0

Explanation: 20% of 50 is 10.
To calculate 20% of a given amount, you can multiply the number by 20 and divide it by 100: 50*20/100 = 10.0

"""Solution"""

bill = int(input())
print(bill*20/100)

#10

Problem

Write a program that checks if the water is boiling.

if Statements


Write a program that checks if the water is boiling.
Take the integer temperature in Celsius as input and output "Boiling" if the temperature is above or equal to 100.

Sample Input
105

Sample Output
Boiling
Do not output anything if the water is not boiling.

"""Solution"""

temp = int(input())
if temp >= 100:
    print("Boiling")
    
#11 

Problem
else Statement


Write a program to control entrance to a club.
Only people who are 18 or older are allowed to enter the club.
Your program takes the age of the person who tries to enter, and outputs "Allowed" if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.

Sample Input
24

Sample Output
Allowed

""" Solution """

age = int(input())
if age >= 18:
    print("Allowed")
else:
    print("Sorry")

    
#12

Problem
Boolean Logic


Given the age of a person as an input, output their age group.

Here are the age groups you need to handle:
Child: 0 to 11
Teen: 12 to 17
Adult: 18 to 64

Sample Input
42

Sample Output
Adult
Remember, you can use the Boolean and operator to combine conditions, like x>0 and x<20.

""" Solution """
age = int(input())
if age <= 11:
    print("Child")
elif age > 12 and age < 18:
    print("Teen")
elif age > 18 and age < 65:
    print("Adult")

    
#13

Problem
while Loops


You are given a program that outputs all the numbers from 0 to 10.
Change the code to make it output only the even numbers.
Any integer that can be divided exactly by 2 is an even number.

""" SOLUTION """

x = 0
while x<=10:
  if x%2 == 0:
   print(x)
  x+=1
    
#14
Problem
continue


You are making a ticketing system.
The price of a single ticket is $100.
For children under 3 years of age, the ticket is free.

Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.

Sample Input
18
24
2
5
42

Sample Output
400
There is one child under 3 among the passengers, so the total price of 5 tickets is $400.

""" SOLUTION """


#15

Sum of Consecutive Numbers


No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.

Let’s save some time by creating a program to do the calculation for you!

Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input
100

Sample Output
5050

Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
You can iterate over a range and calculate the sum of all numbers in the range.
Remember, range(a, b) does not include b, thus you need to use b+1 to include b in the range.

""" SOLUTION """




#16
List Functions


You are working on a queue management program.
The queue is represented by a list.
Write a program to take an input, add it to the end of the queue, and output the resulting list.
The append() method can be used to add new items to the list.

""" SOLUTION """

queue = ['John', 'Amy', 'Bob', 'Adam']

j = queue.append(input())

print(queue)

OR 

queue = ["John’, "Amy", ‘Bob’, "Adam" ]

item = input()
queue. append( item)
print (queue)

#17
String Functions


Your friend sent you a message, however his keyboard is broken and types a # instead of a space.

Replace all of the # characters in the given input with spaces and output the result.
You can use the replace() function of a string to replace one substring with another.

""" SOLUTION """

msg = input()

msg = msg.replace('#',' ')

print(msg)


#18
Functions


We have a function that outputs "Welcome, user" as it is called. We want to make it more personalized, so redesign the given function so that it will take the name of the user as input and output the welcome message with it.

Sample Input
Tommy

Sample Output
Welcome, Tommy
Don't forget to indent the statement in the function.
         
""" SOLUTION """
         
def welcome():
   print("Welcome, " + input())

welcome()
         
OR
         
def welcome():
   print( "Welcome, + name)

name = input()
welcome( )         

#19
Arguments


The given program defines a function printBill(), which takes one string argument and outputs formatted text.
You need to take the user input and call the function by passing the input as its argument.
You need to only call the function, as it will take care of the output.
         
"""SOLUTION """
         
         

#20
Problem

for Loops


for loops allow you to easily iterate through lists.

Given a list of numbers, calculate their sum using a for loop.
Output the sum after the loop

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

print(sum(x)) 

OR

#21
Problem

Ranges


You are creating a date picker for a website and need to output all of the years in a given period.
Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.
The output sequence should start with the first input number and end with the second input number, without including it.

Sample Input
2005
2011

Sample Output
[2005, 2006, 2007, 2008, 2009, 2010]
Convert a range object to a list and output it.

""" Solution """

a = int(input())
b = int(input())

list = list(range(a,b))
print(list)

#22
Problem
List Slices


Write a program that takes a string as input and outputs the last character of that string.
Remember, you can use negative indices to index lists.

""" Solution """

j = str(input())
jj = (j[::-1]); print(jj[0])

OR

str = input()
print(str[-1])




