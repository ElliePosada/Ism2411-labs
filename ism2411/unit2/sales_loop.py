
#Self Assesment
# 1. A for loop is better when you know how many times you want
# something to repeat, while a while loop is better when you want
# something to repeat until a certain condition changes.

# 2. An infinite loop happens when the condition of a while loop
# never becomes false. For example, if I forgot to subtract the
# withdrawal from the balance in Exercise 6, the loop would keep
# running because the balance would never change.

# 3. break stops the loop completely, while continue skips the
# current iteration and moves to the next one. In Exercise 5,
# continue skipped sales of $100 or less, while break stopped
# the loop when the sale was over $400.



#Exercise 1: Sum List
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

#Exercise 2
sales =[120, 80, 250, 175, 90, 410, 60, 215]
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1
average = total / count
print(f"Total: ${total}")
print(f"Count: ${count}")
print(f"Average: ${average}")

#Exercise 3
sales = [120, 80, 250, 175, 90, 410, 60, 215]
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest sale: ${current_max}")

#Exercise 4
sales = [120, 80, 250, 175, 90, 410, 60, 215]
count = 0
total = 0
for sale in sales:
    if sale > 100:
        count += 1
        total += sale
print(f"Sales over $100: {count}")
print(f"Total of those sales: $100: ${total}")

#Exercise 5
sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

#Exercise 6
balance = 1000  
withdrawal = 175
while balance >= withdrawal:
    balance -= withdrawal
    print(f"Withdrew of ${withdrawal} remaining balance: ${balance}")
print(f"Final balance: ${balance}")

#Exercise 7
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end ="\t")
    print()