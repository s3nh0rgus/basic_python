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
user = "major_ussr"
if user not in banned_users:
    print("\n" + user.title() + ", you can post a response if you wish.")
    
print("\n=====Election Day=====")
age = 15
if age >= 16:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18 age!")

print("\n-----Amusement Park-----")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

print("\n=====Topping=====")
requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
