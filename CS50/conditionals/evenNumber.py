def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:      #if there is no remainder of number/2 its even
        return True
    else:
        return False

main()




