'''Computing ASSIGNMENT-3'''

# Question 1 - Python program to count the number of occurrences of each word or character in the string entered by the user as follows: 
from subprocess import list2cmdline


print("\nQuestion-1\n")

str = input("Type Your String: ")
str_set1 = set(str)
str_list = str.split()
str_set2 = set(str_list)
 

if(len(str_list) > 1) :
        for words in str_set2 :
            print("No. of occurrences of", words , 'is ',str_list.count(words))
else :
    for x in str_set1 :
        print("No of Occurrences of", x , 'is ',str.count(x))            

print()
print()


# Question 2 - python script to print next date of input date as follows:
print("\nQuestion-2\n")

year = int(input("Input a year[1800-2025]: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

# months with 31 days = 1,3,5,7,8,10,12  ,  months with 30 days = 4,6,8,11   

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("Next date is: " , day ,"/", month ,"/", year)

print()
print()


# Question 3 - Python program to create a list of tuples with the first element as the number and Second element as the square of the number as follows:
print("Question-3\n")

list = [3,9,10]
print("list = ", list)
tuple = [(x,x**2) for x in list]
print("Output: ", tuple)

print()
print()


# Question 4 - a program to prompt the user for a grade as follows:
print("Question-4\n")

grade = int(input("Enter Your Grade[4-10]: "))
if(grade==4):
    print("Your Grade is 'D' and Poor Performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average Performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average Performance")
elif(grade==7):
    print("Your Grade is 'B' and Good Performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good Performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent Performance")
elif(grade==10):
    print("Your Grade is 'A+' and Outstanding Performance")
else:
    print("Enter A Valid Grade Between 4 to 10")

print()
print()


# Question 5 - a python program to print a pattern as follows:
print("Question-5\n")

a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=11
for i in range(n):
    if 2*i<n:
        j=a[:n-2*i]

        print(" "*i,j)    

print()
print()


# Question 6 -  a  python  script  that  repeatedly  ask  user  to  enter  name  and  SID and then performing further functions on them as follows:
print("Question-6\n")

sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    user_input = input("Do you want to enter another student details(Y or N): ").upper()
    if user_input == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif user_input == 'N':
        break
    else:
     print('Input Is Invalid !!!')

#a-part

print("\n(a) Student Details: " ,students)

#b-part

print("\n(b) Stuident Details Sorted By Names: " ,{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#c-part

print("\n(c) Stuident Details Sorted By SID: " ,{k:v for k,v in sorted(students.items())})

#d-part

search = int(input("\nPlease Enter SID Of The Student You Want To Search: " ))
print("\n(d) Student With The Given SID Is: " ,students[search])


print()
print()


# Question 7 - a python program to print Fibonacci sequence also print average of the resultant Fibonacci series as follows:
print("Question-7\n")

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
terms=int(input("Enter The Number Of Terms In The Seires: "))
if (terms <= 0):    
   print("Plese enter a positive integer!")
else:
   print("Resultant Fibonacci sequence: ")
   sum=0
   for i in range(terms):
       print(fibo(i))
       sum=sum+fibo(i)
avg=float(sum/terms)
print("Average Of The Resultant Fibonacci Series = ",avg)

print()
print()


# Question 8 - Applying Sets Functions As Follows:
print("Question-8\n")

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# a part - a new set of all elements that are in Set1 and Set2 but not both:

A_Set = (Set1|Set2)-(Set1&Set2)
print("(a) Set of all elements that are in Set1 and Set2 but not both: ", A_Set)

# b part - a new set of all elements that are in only one of the three sets Set1, Set2 and Set3:

B_Set = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print("\n(b) Set of all elements that are in only one of the three sets Set1, Set2 and Set3: ", B_Set)

# c part -  a new set of elements that are exactly two of the sets Set1, Set2 and Set3:

C_Set= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)
print("\n(c) Set of elements that are exactly two of the sets Set1, Set2 and Set3: ",C_Set)

# d part - a new set of all integers in the range 1 to 10 that are not in Set1:

D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        D_Set.add(i)
print("\n(d) Set of all integers in the range 1 to 10 that are not in Set1: ", D_Set)

# e part - a new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:

E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        E_Set.add(i)
print("\n(e) Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3: ", E_Set)

print()
print()

print("The End")










 


