#Scientific Calculator
#Shoie Somanath

import math

print "MAIN MENU"
print "1. Addition"
print "2. Subtraction"
print "3. Multiplication"
print "4. Division"
print "5. Modulus"
print "6. Exponentiation"
print "7. Absolute value"
print "8. Factorial"
print "9. Logarithm"
print "10. Round Up"
print "11. Round Down"
print "12. Square Root"
print "13. Trigonometric Functions"
print "14. Inverse Trigonometric Functions"
print "15. Hyperbolic Functions"
print "16. Inverse Hyperbolic Functions"
print
print "NOTE : Please don't choose second number to be zero in" 
print "       case of operations 1-6"
print
op = int(raw_input("Enter the operation you want to perform : "))

if op==1 or op==2 or op==3 or op==4 or op==5 or op==6 :
    a = int(raw_input("Enter first number"))
    b = int(raw_input("Enter second number"))
    dict1 = {1:a+b, 2:a-b, 3:a*b, 4:a/b, 5:a%b, 6:a**b}
    print "The result is : " + str(dict1.get(op))
    
elif op==7 or op==8 or op==9 or op==10 or op==11 or op==12 : 
    a = float(raw_input("Enter the number")) 
    dict2 = {7:math.fabs(a), 8:math.factorial(a), 9:math.log(a), 10:math.ceil(a), 11:math.floor(a), 12:math.sqrt(a)}
    print "The result is : " + str(dict2.get(op))
    
elif op==13 :
    print "Functions Menu"
    print "a. sin"
    print "b. cos"
    print "c. tan"
    fun = raw_input("Choose the function :")
    a = float(raw_input("Enter the angle in radians :"))
    dict3 = {'a':math.sin(a), 'b':math.cos(a), 'c':math.tan(a)}
    print "The result is : " + str(dict3.get(fun))

elif op==14 :
    print "Functions Menu"
    print "d. asin"
    print "e. acos"
    print "f. atan"
    fun = raw_input("Choose the function :")
    a = float(raw_input("Enter the value :"))
    dict4 = {'d':math.asin(a), 'e':math.acos(a), 'f':math.atan(a)}
    print "The result is : " + str(dict4.get(fun))

    
elif op==15 :
    print "Functions Menu"
    print "g. sinh"
    print "h. cosh"
    print "i. tanh"
    fun = raw_input("Choose the function :")
    a = float(raw_input("Enter the angle in radians :"))
    dict5 = {'g':math.sinh(a), 'h':math.cosh(a),'i':math.tanh(a)}
    print "The result is : " + str(dict5.get(fun))    
    
elif op==16 :
    print "Functions Menu"
    print "j. asinh"
    print "k. acosh"
    print "l. atanh"
    fun = raw_input("Choose the function :")
    a = float(raw_input("Enter the value :"))
    dict6 = {'j':math.asinh(a), 'k':math.acosh(a), 'l':math.atanh(a)}
    print "The result is : " + str(dict6.get(fun))    
    
else :
    print "Wrong Choice"    
      
    

