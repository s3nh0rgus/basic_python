#list is a items collection in a particular order

names = ["Gustavo", "Claudio", "Iolanda", "Zilma", "Tiago"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(names[0])
print(numbers[9])
print(names[3].upper())
print(numbers[-1], numbers[-2], numbers[-3])

print("My friend is called " + names[4])

# names[3] = "Vitor"
names.append("Vitor")
print(names)

superheros = []
superheros.append("Superman")
superheros.append("Iron Man")
superheros.append("Batman")
superheros.append("Hulk")
superheros.insert(1, "Wonder Woman")
superheros.insert(2, "Black Panther")
print(superheros)

del superheros[5]
print(superheros)

popped_name = names.pop()
print(names)
print(popped_name)
my_name = names.pop(0)
print(names)
print("My names is " + my_name)

countrys = ["Brazil", "United States", "England", "Japan", "South Korean"]
print(countrys)
imperialist_country = "United States"
# countrys.remove("United States")
countrys.remove(imperialist_country)
print(countrys)

cars = ["bmw", "mercedes", "audi", "tesla"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
bikes = ["mountain", "bmx", "road"]
print("\nOriginal list:") 
print(bikes)
print("\nSorted list:")
print(sorted(bikes))
print("\nOriginal list again:")
print(bikes)

print("\nMy favorite actors: ")
actors = ["adam sandler", "jim carrey", "wagner moura", "lázaro ramos"]
print(actors)
actors.reverse()
print(actors)
print(len(actors))
