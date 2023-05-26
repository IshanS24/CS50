coke = 50
coin = 0
while coke != 0:
    print("Amount Due: " + str(coke))
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        coke = coke - coin
    if coke < 0:
        print("Change owed: " + str(0-coke))
        coke = 0




