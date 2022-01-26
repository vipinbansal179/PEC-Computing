'''Computing ASSIGNMENT-2'''

# Question 1 - Operations on input string as follows: 
print("\nQuestion-1\n")

given_string = "Python is a case sensitive language"
print("String Given :", given_string)

# part (a)
print("Length of String :", len(given_string))

# part (b)
print("String in Reversed Order :", given_string[::-1])

# part (c)
new_string = given_string[10:26]
print("New String :", new_string)

# part (d)
print("Updated String :", given_string.replace("a case sensitive", "object oriented"))

# part (e)
substring_index = given_string.find("a")
print('Index of Substring "a" :', substring_index)

# part (f)
print("String without White Spaces :", given_string.replace (" ", ""))
print()
print()


# Question 2 - Storing data into different variables with help of String formatting and then printing final output:
print("Question-2\n")

name = input("Type your Name: ")
sid = int(input("Type your SID: "))
dept_name = input("Type your Department's Name: ")
cgpa = float(input("Type your CGPA: "))

print()

print("Hey {0} Here!\nMy SID is {1}\nI am from {2} department and my CGPA is {3}.".format(name, sid, dept_name, cgpa))
print()
print()


# Question 3 - Using Bitwise Operator as follows:
print("Question-3\n")

a = 56
print("Value of a =", a)

b = 10
print("Value of b =", b)

# part (a) 
print("a & b =", a&b)

# part (b) 
print("a | b =", a|b)

# part (c)
print("a ^ b =", a^b)

# part (d) 
print("Shifting both a and b with 2 bits to the Left : a-{0},b-{1}".format(a<<2,b<<2))

# part (e) 
print("Shifting a with 2 and b with 4 bits to the Right : a-{0},b-{1}".format(a>>2,b>>4))
print()
print()


# Question 4 - Writting a program to find greatest integer of 3 numbers entered by User as follows:
print("Question-4\n")

num1 = float(input("Type First Number: "))
num2 = float(input("Type Second Number: "))
num3 = float(input("Type Third Number: "))

if (num1 >= num2) and (num1 >= num3):
    greatest_num = num1

elif (num2 >= num1) and (num2 >= num3):
    greatest_num = num2

else:
    greatest_num = num3

print("Greatest of the Three Numbers entered is :", greatest_num)
print()
print()


# Question 5 - Program to check if the word "name" is present in the string entered by the User as follows:
print("Question-5\n")

string = input("Type the String : ")

if ("name" in string):
    print("Yes")

else:
    print("No")
print()
print()


# Question 6 - Program to check if it is possible to form a triangle from length of 3 sides entered by user as input:
print("Question-6\n")

l1 = input("Enter the Length of first side: ")
l2 = input("Enter the Length of second side: ")
l3 = input("Enter the Length of third side: ")

l1 = int(l1)
l2 = int(l2)
l3 = int(l3)

if (l3 >= l1 + l2) or (l2 >= l1 + l3) or (l1 >= l2 + l3):
    print("No")

else:
    print("Yes")

print()
print()






