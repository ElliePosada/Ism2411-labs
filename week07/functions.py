#Self Assessment
#1. The first bug I found was a missing colon in the for loop.
# I noticed it from the error message in the terminal.
# This helped me understand the importance of syntax in Python.
# This showed me that I am still learning how to debug
# code, but I am getting better at understanding errors.

#2. I learned that functions help organize code and
# make it easier to reuse. Instead of writing the
# same calculations multiple times, I can create
# a function and call it whenever I need it.
# This makes my code easier to read and understand.

#3. I learned that global and local variables have
# different scopes in Python. A global variable
# is defined outside a function, while a local
# variable is defined inside a function.
# Changing a local variable does not automatically
# change the global variable, even if they have
# the same name.

#Exercise 1
def calculate_tax(price, rate):
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

#Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
print(f"gold: ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none: ${apply_discount(200, 'none'):.2f}")

#Exercise 3
discounted = apply_discount(200, "gold")  
print(f"After gold discount: ${discounted:.2f}")

tax = calculate_tax(discounted, 0.07)
total = discounted + tax
print(f"After tax: ${total:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
print(f'final price(200, "gold", 0.07) =  ${final_price(200, "gold", 0.07):.2f}')

#Exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Final price for ${price} with {tier} tier: ${total:.2f}")

#Exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

#Exercise 6
x = 100 #global variable
def double_it():
    x = 999 #local variable - different from the global x!
    return x * 2
print(x)
print(double_it())
print(x)
# A global variable is defined outside a function. A local variable is defined inside a function.
# The x inside double_it() is separate from the
# global x, so the original value stays 100.