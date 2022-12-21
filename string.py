name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "gustavo"
last_name = "barros"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

print("Programming Languages: \n\tPython\n\tJavScript\n\tPHP")

favorite_language = "    python "
print(favorite_language)
favorite_language = favorite_language.rstrip().lstrip() # eliminas os espaços em branco da direita (rIGHT) e da esquerda (lEFT) também.
print(favorite_language)