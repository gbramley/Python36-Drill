#Assign an integer to a variable
x = 15
y = 5
z=0


#Assign a string to a variable
name = "Gavin"
print name.upper()

#Assign a float to a variable

y= float(15)/float(3)
print y

#Use the print function and .format() notation to print out the variable you assigned

s = "Hello, Gavin"
str(s)
print('Today is {}'.format(s))


#Use each of the operators +,-,*,/,+=,=,%


print (x+y)
print (x-y)
print (x*y)
print (x/y)
z += x
print "Value of z is ", z

z = x + y
print "Value of z is", z

print "Hello it is %d oclock and I am %d yrs old" % (2, 33)

#Use of logial operators: and, or, not

if (x >= 15) and (y > 4):
    print "True"

w = 15
if not (w < 1) or (w > 35):
    print "false"

#Use of conditonal statments: if, elif, else

x = 14
if x ==15:
    print 'x = 15'
elif x == 9:
    print 'x = 9'
else:
    print 'x does not equal 9 or 15'


#use of a while loop

counter = 10
while counter < 15:
    print counter
    counter = counter + 1

#use of a for loop
for counter in range (10,15):
    print counter

#create a list and iterate through that list
#to print each item out on new line

name_of_friends = ['Liese Chapman', 'Matt Huiskamp', 'Walter Colt',]
print "My great friends are: " + name_of_friends[0]
print "My great friends are: " + name_of_friends[1]
print "My great friends are: " + name_of_friends[2]
for friend in name_of_friends:
    print "My great friends are: " + friend
#Create a tuple and iterate through it using a for loop to
#print each item out on new line

for z in (1,2,3):
    print z

#Define a function that returns a string variable
x=15
y=5
def subtraction(x):
    subtract = x - y
    return subtract
toSubtraction = (20)
subtractResult = subtraction(toSubtraction)
print "The result of  " + str(toSubtraction) + " subtract  " +str(y) + " is " +str(x)

x = 10
y = 100

def square(x):
    y = x * x
    return y
toSquare = 10
squareResult = square(toSquare)
print "The result of " +str(toSquare) + " squared is " +str(squareResult)

#Call the function you defined above and print the result to the shell

import SubtractionInfo
print SubtractionInfo.subtraction(x)