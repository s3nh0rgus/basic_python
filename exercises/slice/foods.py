foods = ["burguer", "pizza", "chocolate", "donut", "spaghetti"]
favorite_foods = foods[:]
foods.append("barbecue")
favorite_foods.append("french fries")

for food in foods:
    print("The best food is " + food.title())

print("\n")

for food in favorite_foods:
    print("My favorite food is " + food.title())