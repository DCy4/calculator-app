from replit import clear

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
def calculator():
  num1 = float(input("What is the first number? "))
  #loop through keys to print symbols
  for symbol in operation:
    print(symbol)
  should_continue = True
  
  while should_continue:
    #find the key to pair with value 
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the second number? "))
    #calculation_function used to create name part of function without '()'
    calculation_function = operation[operation_symbol]
    #answer variable replaces calculation_function + "(num1,num2)"
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    user_choice = input(f"Type 'y' to continue claculating with {answer},  type 'n' to start a new calculation, or 'c' to clear screen: ")
    if user_choice == 'y':
      num1 = answer
    elif user_choice == 'c':
      clear()
    else:
      should_continue = False
      calculator()

#initial funct call
calculator()