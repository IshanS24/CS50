
airline = [["BCN", "Barcelona International"], ["DUB", "Dublin"], ["LIS", "Lisbon"], ["LHR", "London Heathrow"]]

code = input("Input Code: ")
index = 0

while airline[index][0] != code:            #2nd digit is column, first is row
    index = index + 1

print("The code", code, "is", airline[index][1])
