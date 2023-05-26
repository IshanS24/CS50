tweet = str(input("Input: "))

print("Output: ", end="")

for i in tweet:
    if i.lower() in ['a','i','o','e','u']:
        print("", end="")
    else:
        print(i, end="")






