cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

ingredient = "pepperoni"
if ingredient != "cheese":
    print("\nHold the cheese")
    
answer = 7
if answer != 42:
    print("\nThat's not the correct answer. Please try again!") 

banned_users = ["weth3people", "bolsonaro2022", "kanyewest2024"]
user = "major_ancap"
if user not in banned_users:
    print("\n" + user.title() + ", you can post a response if you wish.")