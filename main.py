#Add
def add(n1, n2):
  return n1 + n2
#subtract
def subtract(n1, n2):
  return n1 - n2
#multiply
def multiply(n1, n2):
  return n1 * n2
#divide
def divide(num, den):
  return num / den

#Dictionary {symbol: function name}
operation = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

#loop through keys to print symbols
for symbol in operation:
  print(symbol)
#find the key to pair with value 
operation_symbol = input("Pick an operation from the line above: ")
#calculation_function used to create name part of function without '()'
calculation_function = operation[operation_symbol]
#answer variable replaces calculation_function + "(num1,num2)"
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operation[operation_symbol]
second_answer = calculation_function(calculation_function(num1,num2), num3)