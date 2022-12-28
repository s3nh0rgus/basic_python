programmers = ["linus torvalds", "richard stallman", "john carmark", 
               "guido van rossum"]

for programmer in programmers:
    print(programmer.title() + " was part of computer history")

print("Thanks for good work") 

# function range(start;end)
for i in range(1,6): 
    print(i)
# DISCLAIMER: when i arrive in 6, the loop stop and do not show 6. This is 
# like navigation in a list: [0, 1, 2, 3...], but in this case the problem 
# of 1 is +1 while in list is -1. 

numbers = list(range(1,6))
print(numbers)

# even or odd
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# exponentiation
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

#basic statistics
list_of_int = [1, 2, 3, 4, 5]
print(min(list_of_int))
print(max(list_of_int))
print(sum(list_of_int))

#list comprehension
squares = [value ** 2 for value in range(1,11) ]
print(squares)
