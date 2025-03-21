a=input('Enter First Number:')
b=input('Enter Second Number:')
print('Menu(Press a number to select an operation)')
print('1.SUM \n2.SUBTRACTION \n3.DIVISION \n4.MULTIPLY \n')

def sum(a,b):
    c=int(a)+int(b)
    print(c)
    
def subtraction(a,b):
    c=int(a)-int(b)
    print(c)   

def division(a,b):
    c=int(a)/int(b)
    print(c)    

def multiply(a,b):
    c=int(a)*int(b)
    print(c)    

inp=int(input())
if inp==1 :
    sum(a,b)
else :
    if inp==2 :
        subtraction(a,b)

