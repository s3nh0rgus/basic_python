alien_color = 'green'
if alien_color == "green":
    print("You just earned 5 points!")
if alien_color == "red":
     print("You just earned 7 points!")

print("\n")
alien_color = 'red'
if alien_color != "green":
    print("You just earned 15 points!")
else:
    print("You just earned 5 points!")

print("\n")    
alien_color = 'green'
if alien_color == "green":
    print("You just earned 5 points for hitting the alien!")
else:
    print("You just earned 10 points")
alien_color = 'yellow'
if alien_color == "green":
    print("You just earned 5 points for hitting the alien!")
else:
    print("You just earned 10 points")

print("\n")
alien_color = 'yellow'
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
elif alien_color == "red":
    print("You just earned 15 points!")
else:
    print("No color == 0 points.")