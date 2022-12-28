guests = ["Albert Einstein", "Nikola Tesla", "Mom", "Tiago"]
print("You were invite to my wedding, " + guests[0])
print("Please! You have to come to my wedding, " + guests[1])
print("You will be at my wedding, just as you were every moment of my life, " 
      + guests[2])
print("You will be the best man at my wedding, " + guests[3])

print("Unfortunately " + guests[1] + " will not be able to attend my wedding."
      + "\n")
del guests[1]
guests.append("Ada Lovelace")
print("I need genie at my wedding, " + guests[0])
print(guests[1] + ", come to my wedding")
print(guests[2] + ", side by side, always together! Even at my wedding.")
print(guests[3] + ", please! Come to my wedding.\n")

print("Just now, I found a bigger table and ended up inviting three more people.")
guests.insert(0, "Dad")
guests.insert(3, "Carol")
guests.append("Pepe Moreno")
print("You're dumbass, but I love you. Please, come to my wedding!" + guests[0])
print("That human stupidity does not prevent you from going to my wedding, " +
      guests[1])
print("See you at my wedding, " + guests[2])
print("For old times' sake, come to my wedding " + guests[3])
print(guests[4] + ", be at my wedding")
print("Mark your presence at my wedding, as you marked in my story " + guests[5])
print(guests[6] + " make noise with the Risca Faca!\n")

print("I just learned that the guest table was not successful in its purchase,"
    + " so I will only to invite two people.")
print("I am sorry! I hope that you can understand " + guests.pop(1))
print("I am sorry! I hope that you can understand " + guests.pop(2))
print("I am sorry! I hope that you can understand " + guests.pop(2))
print("I am sorry! I hope that you can understand " + guests.pop(2))
print("I am sorry! I hope that you can understand " + guests.pop())
print("If you are not my wedding " + guests[0] + " and " + guests[1] + 
      ", there is no wedding.\n")

guests_dinner = len(guests)
print("I will be having dinner with my " + str(guests_dinner) + 
      " wedding guests (my " + guests[0] + " and " + guests[1] + ").\n")

del guests[0]
del guests[0]
print(guests)
