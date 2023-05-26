def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    floatnum = d.replace("$", "")   #replaces dollars to nothing
    return float(floatnum)

def percent_to_float(p):
    floatpercent = p.replace("%", "")
    floatpercent = float(floatpercent) / 100
    return floatpercent

main()




