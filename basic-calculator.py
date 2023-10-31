#This is a basic calculator. I'm bored, haha!
online = 1
 
while online == 1: 
  number1 = float(input("insert the first number: "))
  operator = input("insert the operator: ") # + | - | * | /
  number2 = float(input("Insert the second number: "))
    
  operator = operator
  if operator == "+":
    result = number1+number2
    print("The result is ", result)
  elif operator == "-":
    result = number1-number2
    print("The result is ", result)
  elif operator == "*":
    result = number1*number2
    print("The result is ", result)
  elif operator == "/":
    if number2 != 0:
      result = number1/number2
      print("The result is ", result)
    else:
      print("Error! Division by zero.")
  else:
    print("Error! Invalid values entered.")
    
  online = int(input("Do you need another calculation? [1]Yes / [0]No: "))
  if online == 0:
    break