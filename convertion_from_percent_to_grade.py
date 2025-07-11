print("****THIS IS TO CONVERT YOUR MARK TO YOUR GRADE****")
a=float(input("ENTER YOUR TOTAL MARK:"))
b=a/500*100
if(b>=90):
    print("YOUR GRADE IS A+")
elif(b>=80):
    print("YOUR GRADE IS A")
elif(b>=70):
    print("YOUR GRADE IS B+")
elif(b>=60):
    print("YOUR GRADE IS B")
elif(b>=50):
    print("YOUR GRADE IS C+")
elif(b>=35):
    print("YOUR GRADE IS C")    
else:
    print("YOUR GRADE IS F")
