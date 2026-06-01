def addition():

  value_addition_01 = int(input("Add the first number to start the addition:\n"))
  value_addition_02 = int(input("Add the second number and press enter to view the result:\n"))
  addition_result = value_addition_01 + value_addition_02
  
  print(f"The result of the addition is = " + str(addition_result))

def sustraction():
  value_sustraction_01 = int(input("Add the first number to start the sustraction:\n"))
  value_sustraction_02 = int(input("Add the second number and press enter to view the result:\n"))
  sustraction_result = value_sustraction_01 + value_sustraction_02
  
  print(f"The result of the sustraction is = " + str(sustraction_result))

def multiplication():
  value_product_01 = int(input("Add the first number to start the multiplication:\n"))
  value_product_02 = int(input("Add the second number and press enter to view the result:\n"))
  product_result = value_product_01 * value_product_02
  print("The result of the product is = " + str(product_result))

addition()
sustraction()
multiplication()