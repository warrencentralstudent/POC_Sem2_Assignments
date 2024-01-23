number1 = int(input("Enter a number for division: "))
number2 = int(input("Enter another number for division: ")) 
try:
   
    print("The answer is",number1/number2)
except ZeroDivisionError:  
    print('You provided 0 and division by 0 is not possible, sorry')
except:
    print('Something strange happened here, sorry')

