#!/usr/bin/env python
# coding: utf-8

# In[3]:


def buy(costs , coffee ,water , milk , cups):
    n = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if n == 1:
        coffee = coffee - 16
        water = water - 250
        costs = costs + 4
        cups = cups - 1
    elif n == 2:
        coffee = coffee - 20
        milk = milk - 75
        water = water - 350
        costs = costs + 7
        cups = cups - 1
    elif n == 3:
        coffee = coffee - 12
        milk = milk - 100
        water = water - 200
        costs = costs + 6
        cups = cups - 1
    print("The coffee machine has:\n" + str(water) + " of water" + "\n" + str(milk) + " of milk" + "\n" + str(coffee) + " of coffee beans" + "\n" + str(cups) + " of disposable cups" + "\n" + str(costs) + " of money",)
    

def fill(costs , coffee ,water , milk , cups):
    wat = int(input("Write how many ml of water do you want to add:"))
    mi = int(input("Write how many ml of milk do you want to add:"))
    co = int(input("Write how many grams of coffee beans do you want to add:"))
    cu = int(input("Write how many disposable cups of coffee do you want to add:"))
    water = water + wat
    milk = mi + milk
    coffee = coffee + co
    cups = cups + cu
    print("The coffee machine has:\n" + str(water) + " of water" + "\n" + str(milk) + " of milk" + "\n" + str(coffee) + " of coffee beans" + "\n" + str(cups) + " of disposable cups" + "\n" + str(costs) + " of money",)
    
def take(costs):
    print("I gave you " + str(costs) + " $")
    costs = 0
    print("The coffee machine has:\n" + str(water) + " of water" + "\n" + str(milk) + " of milk" + "\n" + str(coffee) + " of coffee beans" + "\n" + str(cups) + " of disposable cups" + "\n" + str(costs) + " of money",)




# In[4]:


water = 400
milk = 540
coffee = 120
cups = 9
costs = 550
print("enter 'buy' to buy  , 'fill' to fill the machine or 'take' to take the money out ")
 
action = input()
print("""The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money""")
if action == "buy":
    buy(costs , coffee ,water , milk , cups)
elif action == "fill":
    fill(costs , coffee ,water , milk , cups)
elif action == "take":
    take(costs)




# In[ ]:




