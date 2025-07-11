print("****This Programm Is To Check The Divisiblity of A Number****")
a=int(input("Enter The Value Of Dividend:"))
b=int(input("Enter The Value Of Divisor:"))
c=a%b
if(c==0):
    print(a,"Is Divisible By",b)
else:
    print(a,"Is Not Divisible By",b)
