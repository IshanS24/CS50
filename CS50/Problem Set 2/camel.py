#program

name = str(input("camelCase: "))
for i in name:
    if i.isupper():
        name = name.replace(i, f"_{i.lower()}")
        print("snake_case: " + name)




