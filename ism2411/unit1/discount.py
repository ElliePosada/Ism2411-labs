#Self-Assesment Questions
#1. When order_total = 350, the program checks the discount conditions in order. It first checks whether 350 falls into the lowest discount tier. If it does not, it moves to the next condition. Since 350 is greater than 100 and less than 500, it meets the condition for that tier. The program then applies the discount associated with that range and skips any remaining elif conditions.
#2. if total > 100 and total < 500: checks both conditions together. The code inside the if statement only runs when the total is both greater than 100 and less than 500. Two separate if statements are different because Python evaluates each one independently, meaning the code under one condition could run even if the other condition is false. Therefore, they would not necessarily produce the same result.
#3. I encounter tiered conditional logic in everyday situations such as shipping fees. For example, a store might charge a shipping fee for smaller purchases, offer cheaper shipping after a certain amount, and provide free shipping when the order reaches a higher amount. Learning Python conditionals helps me understand that these systems can be represented as a series of conditions where the outcome depends on which range a value falls into.

#Starter code from Lab 5

total = float(input("Enter cart total: $"))
# Add your if/elif/else here

# Exercise 1
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.1
elif total >= 100:
    discount = 0.05
else:
    discount = 0        

#discount = 0 # replace with correct logic 
final=total*(1-discount)
print(f"Discount: {discount*100:.0f}%")

#Exercise 2
if final > 1000:
    status = "manager_approval_required"
else: 
    status = "auto_approved"    

print(status)

#Exercise 3
region = input("Enter region: ")
extra_discount = 0

if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")

final=total * (1 - (discount + extra_discount))
print(final)

#Exercise 4

customer_type = "wholesale"
if region == "South" and total > 100 and customer_type == "wholesale"
    extra_discount = 0.03

#Exercise 5
amount = 0
if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE -- REVIEW REQUIRED")

#Exericse 6

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False #bool

vip_upgrade = True
if (total_spent_this_year > 2000 or orders_this_year > 10) and not has_outstanding_balance:

    vip_upgrade = True 
else:
    vip_upgrade = False  