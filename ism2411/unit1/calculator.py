#self assessment questions
#1. If I forgot to divide the discount percentage by 100, and used 10 instead of 0.10, python would not crash. The program would still run, but it would calculate a much larger discount and give a wrong answer.
# 2. Another business scenario would be packing products into shipping boxes. Division could tell me how many full boxes I can pack, and the modulo operator
#  could tell me how many products are left over that do not fill a complete box.
# 3. I feel least confident about formatting numbers correctly with f-strings. More practice with different formatting examples, such as money and
#  percentages, would help me become more confident with it.

# revenue, margins and discount calculator

#Exercise 1
from itertools import product


price = 50
quantity = 12
revenue = price * quantity

print(f"Revenue: ${revenue:,.2f}")

#Exercise 2

cost = 30
price = 50
margin = (price - cost) / price
print(f"Margin: {margin:.1%}")

#Exercise 3; Boolean Logic
#product A wins if margin_a > margin_b
# Product A margin_a = 0.60
# Product_b margin_b = 0.25
margin_a  = 0.60
margin_b = 0.25
margin_a_wins = margin_a > margin_b
print(f"Product A wins: {margin_a_wins}")

#  Exercise 4: logic combo
is_premium = price > 100 and margin > 0.3
print(f"Is premium: {is_premium}")

price = 150
margin = .35

# Exercise 5: Division + Mod 

print(17/3) # 5.666666666666667
print(17//3) # 5
print(17%3) # 2

#Exericse 7:

BOX_SIZE = 24 #ALL UPPER CASE MEANS CONSTANT 
items_ordered = int(input("Number of items ordered: "))
full_bpxes = items_ordered // BOX_SIZE
lose_items = items_ordered % BOX_SIZE
exact_fit = loose_items ==0
print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")

#Exercise 6: 
def calc_discount( price, rate): 
    return price * (1-rate) # gives up the answer 
print(calc_discount(100, 0.2))
discounted_pct = 20
discounted_rev = revenue * (1 - discounted_pct / 100)
print(f"Discounted revenue: ${discounted_rev:,.2f}")

#inputs name, retail_price, cost, quantity,_sold, discount_rate 
retail_price = float(input("Enter retail price: "))
cost = int(input("Enter cost: "))
quantity_sold = int(input("Enter quantity sold: "))
discount_pct = float(input("Enter discount rate: "))
cost = float(input("Enter the discount percentage: "))
print("="*50))
evenue = retail_price * quantity_sold
discounted_revenue = revenue * (1 - discount_pct / 100)
gross_margin = (retail price - cost) / retail_price
net_profit = discounted_revenue - (cost * quantity_sold)

#Outputs
print(f"Product: {product}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Discounted revenue: ${discounted_rev:,.2f}")
print(f"Gross margin: {gross_margin:.1%}")
print(f"Net profit: ${net_profit:,.2f}")
