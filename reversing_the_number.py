print("******** REVERSING FUNCTION*********")
x=int(input("ENTER THE NUMBER TO BE REVERSED:"))
rev=0
while(x>0):
    y=x%10
    rev=rev*10+y
    x//=10
    
print("the reversed number is",rev)
print("*********END***********")
