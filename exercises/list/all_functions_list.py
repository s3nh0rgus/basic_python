southeastern_states_brazil = ["são paulo", "rio de janeiro", "espirito santo", "bahia"]
southeastern_states_brazil.append("minas gerias")
print(southeastern_states_brazil.pop(3).title() + " it's not a state in southeastern Brazil.\n")

print("Countrys of South America:")
south_america_countrys = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Uruguay"]
south_america_countrys.append("Venezuela")
south_america_countrys.insert(8, "Peru")
south_america_countrys.insert(7, "México")
print(south_america_countrys)
print("\n\tOps! Something wrong... Let's fix it!\n")
del south_america_countrys[7]
print(south_america_countrys)

print("\nI am from " + south_america_countrys[2] + ".")

print("\n==Some functions of list in Python==\n")
letters = ["f", "b", "d", "a", "g", "e", "c"]
print("Sorted:")
print(letters)
print(sorted(letters))
print(letters)
print(sorted(letters, reverse=True))
print(letters)
print("\nSort:")
letters.sort()
print(letters)
letters.sort(reverse=True)
print(letters)
print("\nReverse:")
letters.reverse()
print(letters)
letters.reverse()
print(letters)
print("\nLen:")
print(len(letters))
