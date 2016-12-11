#Basic Calculator
#Shoie Somanath

print "MAIN MENU"
print "1. Addition"
print "2. Subtraction"
print "3. Multiplication"
print "4. Division"
print "5. Modulus"
print "6. Exponentiation"
print "7. Absolute value"
print
op = raw_input("Enter the operation you want to perform : ")

def Add() :
    a = int(raw_input("Enter first number"))
    b = int(raw_input("Enter second number"))
    print "Your choice is Addition"
    print "a = " + str(a) + " and b = " + str(b)
    print "The sum is " + str(a+b)
    
def Sub():
    a = int(raw_input("Enter first number"))
    b = int(raw_input("Enter second number"))
    print "Your choice is Subtraction"
    print "a = " + str(a) + " and b = " + str(b)
    print "The difference is " + str(a-b)

def Mul():
    a = int(raw_input("Enter first number"))
    b = int(raw_input("Enter second number"))
    print "Your choice is Multiplication"
    print "a = " + str(a) + " and b = " + str(b)
    print "The product is " + str(a*b)

def Div():
    a = int(raw_input("Enter first number"))
    b = int(raw_input("Enter second number"))
    print "Your choice is Division"
    print "a = " + str(a) + " and b = " + str(b)
    print "The quotient is " + str(a/b)

def Mod():
    a = int(raw_input("Enter first number"))
    b = int(raw_input("Enter second number"))
    print "Your choice is Modulus"
    print "a = " + str(a) + " and b = " + str(b)
    print "The remainder is " + str(a%b)

def Exp():
    a = int(raw_input("Enter first number"))
    b = int(raw_input("Enter second number"))
    print "Your choice is Exponentiation"
    print "a = " + str(a) + " and b = " + str(b)
    print "The Exponent is " + str(a**b)

def AbsVal():
    a = float(raw_input("Enter the number"))
    print "Your choice is Absolute Value"
    print "The absolute value of " + str(a)+ " is " + str(abs(a))

if op=='1':
    Add()
elif op=='2':
    Sub()
elif op=='3':
    Mul()
elif op=='4':
    Div()
elif op=='5':
    Mod()
elif op=='6':
    Exp()
elif op=='7':
    AbsVal()  
else:
    print "Wrong Choice"    