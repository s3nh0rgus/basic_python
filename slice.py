players = ["gustagod", "bazarov", "maradona10", "aktrova0"]
print(players[0:3])
print(players[1:4])
print(players[:2])
print(players[2:])
print(players[-3:])

print("\nHere are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

foods = ["burguer", "pizza", "chocolate", "donut", "spaghetti"]
favorite_foods = foods[:]
print("\nFoods:")
print(foods)
print("My favorite foods:")
print(favorite_foods)

foods.append("barbecue")
favorite_foods.append("french fries")
print("\nFoods:")
print(foods)
print("My favorite foods:")
print(favorite_foods)
# Why isn't this (foods = favorite_foods) method copying one list to another? Because, when you use this method just is coupling other variable to one list,
# that already is coupling with one variable, then these two variable are sharing the same list. If you want a new list copy of another list, use slices!
