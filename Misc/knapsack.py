import random

# My noob attempt at the Knapsack problems.
"""
def greedy(items, limit):
    # Initializing an empty list for adding items.
    knapsack = []
    current_level = 0

    for r in range(len(items)):
        # Choosing and adding biggest item from currently available items.
        current_highest = max(items.keys())
        current_level += items[current_highest]
        knapsack.append(current_highest)

        # Checking limit. If exceeded, removing the last added item from knapsack.
        if current_level >= limit:
            current_level -= items[current_highest]
            knapsack.remove(current_highest)
        
        # Removing the last added item, which was the highest, to find the next.
        items.pop(current_highest)
    
    return knapsack
"""

class Jewel(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def getValue(self):
        return self.value

    def getName(self):
        return self.name
    
    def __str__(self):
        return "<", self.name,",",self.value,">"

# This function returns a list if Jewel objects using names and prices.
def buildList(names, prices):
    items = []
    for r in range(len(names)):
        items.append(Jewel(names[r], prices[r]))

    return items

# We go through each node of the Binary Tree, looking at each possible combo and its value and comparing it at each node.
# The best result drips down (in this case, up) and we get the best result.
def binaryTreeSearch(items, limit):
    if len(items) == 0 or limit == 0:
        return [], 0
    elif items[0].getValue() > limit:
        return binaryTreeSearch(items[1:], limit)
    else:
        current = items[0]
        withCurrent, withCurrentValue = binaryTreeSearch(items[1:], limit - current.getValue())
        withCurrent.append(items[0].getName())
        withCurrentValue += current.getValue()

        withoutCurrent, withoutCurrentValue = binaryTreeSearch(items[1:], limit)

        if withCurrentValue > withoutCurrentValue:
            return withCurrent, withCurrentValue
        else:
            return withoutCurrent, withoutCurrentValue

names = ["Diamond", "Ruby", "Sapphire", "Emerald", "Opal", "Turqoise"]
prices = [800, 600, 300, 650, 250, 200]
limit = 2000
items = buildList(names, prices)
choosenItems, ItemsValue = binaryTreeSearch(items.copy(), limit)
print(choosenItems)
print(ItemsValue)