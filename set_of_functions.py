print("********panlindrome function*******")
str1=input("ENTER THE WORD:")
str2=str1[-1: :-1]
if(str1==str2):
    print(str1,"is palindrome")
else:
    print(str1,"is not palindrome")
print("*******end*******")

print("********reversing function*******")
str1=input("enter the word:")
for i in range(-1,-len(str1)-1,-1):
  print(str1[i])
print("*********end**********")

print("******replacing function************")
str1="sanjay is the"
str1.replace(" ","_")
print("***********end***********")

print("***********number of words function************")
str1=input("enter the word:")
count=0
for i in str1:
    count=count+1
print(count)
print("***********end********")

print("*******verifing function*********")
x=int(input("enter the first angle:"))
y=int(input("enter the second angle:"))
z=int(input("enter the third angle:"))
a=x+y+z
if(a==180):
    print("these angle form a triangle")
else:
    print("these angle does not form a triangle")
print("**********end*********")

print("********squaring function***********")
x=int(input("enter the number:"))
print("n is",x,",","n square is",x*x,",","n cube is",x*x*x,",","n power four is",x*x*x*x,".")      
print("*******end*************")

print("************verifing function***********")
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
            print(num, "is a prime number")
print("***********end**********")

print("***********number of vowels***********")
x=input("Enter a word: ")
vowels="aeiouAEIOU"
count=0

for i in x:
    if i in vowels:
        count=count+1

print("Number of vowels:", count)
print("***********end**********")

print("**********bmi fuction***********")
x=float(input("Enter your height in meters: "))
y=float(input("Enter your weight in kilograms: "))
z=x/y**2
if z < 18.5:
    print("You are underweight.")
elif 18.5 <= z < 24.9:
    print("You have a normal weight.")
elif 25 <= z < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
print("********end**********")    
