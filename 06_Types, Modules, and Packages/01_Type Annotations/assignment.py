#add type annotation on the functions and variables
#variables types are float, function return type is a float

def average(a : float, b: float) -> float:
    return (a + b) / 2 

number1 : float = float(input("Enter a decimal number: "))
number2 : float = float(input("Enter another decimal number: "))
print(average(number1, number2))
