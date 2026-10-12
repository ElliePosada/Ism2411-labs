# Exercise 5: Investigation Observations
# type("12") returned str because "12" is the text inside quotation marks.
# type (12) returned int because 12 is a whole number number.
# type(12.0) returned float because 12.0 is a decimal numnber
# type(True) returned bool because True is a Boolean value.
# "5" + "3" returned "53" because strings are joined together instead of added.
# 5 + 3 returned 8 because integers are added as numbers.
# bool("False") returned True becaue a non-empty string is considered True.
# bool("") returned False because an empty string is considered False.
# bool(0) returned False because 0 is considered False.
# bool(1) returned True because a non-zero number is considered True
# int("7") returned 7 because the string "7" is converted to an integer.
# float("7.2") returned 7.2 because the string "7.2" is converted to a float.
# int(7.9) returned 7 because converting a float intp an integer removes the decimal portion
# str(42) returned "42" because the integer 42 was converted to a string.

#Self Assesement Questions: 
# 1. When I forgot to convert the price from a string to a float, Python gave a TypeError because it could not preform the math using a string and a number. The error occured because input()returns a string , so the price needed to be a float first.
# 2. "5" + "3" returned "53" because Python treats values in quotation marks as strings, and joins them together instead of adding. Since input() returns a string , it must be converted to a number such as an int or float before doing math.
# 3. In supply chain management, I could build a tool that calculates the toal cost of an order using varibles for price and quantity. I could use number types for calculations and f-strings to display the order information and total cost in an easy-to-read format.


#Exercise 1: Varibles and Types
product = "Notebook"
unit_price = 4.99
quantity = 12
in_stock = True 

# Exercise 2: f-string practice
print(type(product))
print(type(unit_price))
print(type(quantity))
print(type(in_stock))
print(f"{quantity} units of {product} at ${unit_price} each will cost ${unit_price * quantity}")\

#Execise 3: Input version
product=input("Enter product: ")
unit_price=float(input("Enter unit price: "))
quantity=int(input("Enter quantity: "))
in_stock=bool(input("Is the product in stock? (True/False): "))

#Exercise 4: Multi-Varible product card
product = "Notebook"
unit_price = 4.99
quantity = 12
unit_cost = 3.29
revenue = unit_price * quantity
margin = (unit_price - unit_cost)/unit_price 
print(f"product: {product}")
print(f"price: ${unit_price}")
print(f"Qty: {quantity}")
print(f"Revenue: ${revenue}")
print(f"margin: {margin:.1%}")


