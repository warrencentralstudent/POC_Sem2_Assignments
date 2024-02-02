number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
except ValueError:
    print("I can't work with nothing.")
try:
    answer = number1/number2
    print ("The quotient is", answer)
except ZeroDivisionError:  
    print('You provided 0 and division by 0 is not possible, sorry')
else:
    print("No problem here!")
finally:
    print("Howdy :)")

