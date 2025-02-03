print('----------Welcome To Calculator----------\n')

print(' +  =  Addition\n','-  =  Substraction\n','*  =  Multiplication\n','/  =  Division\n','%  =  Modular Division\n','** =  Exponent\n','// =  Floor Division\n') 

num1 = float(input('Enter the First number : '))
num2 = float(input('Enter the Second number : '))

#opr = operator 
opr = input('Enter the operator from +,-,*,/,%,**,// : ')

if opr =='+' :
    print('Addition of two numbers is : ',num1 + num2)
    
elif opr == '-' :
    print(num1 - num2)
    
elif opr == '*' :
    print('Multiplication of two numbers is : ',num1 * num2)
    
elif opr == '/' :
    print('Division of two numbers is : ',num1 / num2)
    
elif opr == '%' :
    print('Modular Division of two numbers is : ',num1 % num2)
  
elif opr == '**' :
    print('Exponent of two numbers is : ',num1 ** num2)
    
elif opr == '//' :
    print('Floor Division of two numbers is : ',num1 // num2)
    
else:
    print('Invalid input')
    
print('\n------------------Thank You------------------')
print('\n-----------------Visit Again-----------------')
