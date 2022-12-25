cubes = []
i = 0
for number in range(1, 11):
    cubes.append(number**3)
    print(cubes[i])
    i = i + 1

# list comprehension  
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)