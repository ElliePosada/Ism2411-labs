# Reflection Question 1:
# I was surprised by how easily Python lists can store and organize
# multiple values in one place. I also learned that I can use loops
# to go through a list instead of working with each value separately.

# Reflection Question 2:
# When I worked at Publix, Python lists could have helped organize
# sales information and track transactions. Instead of manually
# reviewing data in Excel, I could use Python to calculate totals
# and averages more efficiently.


#Exercise 1
print("---Exercise 1: Build a List---")
Inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(Inventory)
print(len(Inventory))

#Exercise 2: index Practice
print("---Exercise 2: Index Practice---")
print(Inventory[0]) #grabs first item
print(Inventory[-1]) #grabs last item

middle = len(Inventory) // 2
print(Inventory[middle]) #grabs middle item

#Exercise 3
print("---Exercise 3: Add to the List---")

print (Inventory[3]) # grabs the first three items
print (Inventory[-2]) # grabs the last two items
print(Inventory[::2]) # grabs every second item

#Exericse 4: List Methods
print("---Exercise 4: List Methods---")

Inventory.append("envelope")
Inventory.append("")
print(Inventory)

Inventory.remove("tape")
print(Inventory)

Inventory.sort()
print(Inventory)

#Exercise 5: Tuple Comparison
print("---Exercise 5: Tuple Comparison---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident or on purpose.")
")
#Exercise 6: List Average Sales
print("---Exercise 6: List Average Sales---")

sales = [100, 250, 75,480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sale: {average:.2f}")
print(f"best sale: {max(sales)}")
print(f"worst sale: {min(sales)}")

#Exercise 7
print("---Exercise 7: Accumalator pattern---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted =[]
for price in prices:
   discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

#Exercise 8
print("---Exercise 8: Filter---")
sales = [340, 127, 589, 204,467, 88, 731,315,62,490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales)/len(high_sales):.2f}")
