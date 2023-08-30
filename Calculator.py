def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

while True:

     num1 = float(input("Enter first number: "))
     choice = input("Enter operator: ")
     num2 = float(input("Enter second number: "))

     match choice:
          case "+":
               print(num1, "+", num2, "=", add(num1, num2))
          case "-":
               print(num1, "-", num2, "=", subtract(num1, num2))
          case "*":
               print(num1, "*", num2, "=", multiply(num1, num2))
          case "/":
               print(num1, "/", num2, "=", divide(num1, num2))
          case _:
               print("Invalid input try again:")
               continue
     if input("Press any key for continue and only 'Enter' for exit : "):
          continue
     exit("Thanks for using calculator.")