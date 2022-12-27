pizzas = ["portuguesa", "calabresa", "pepperoni", "quatro queijos"]
friend_pizzas = pizzas[:]
pizzas.append("brocolis")
friend_pizzas.append("bacon")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("\nMy friend's favorite pizza  is:")
for pizza in friend_pizzas:
    print(pizza.title())