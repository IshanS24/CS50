def main():
    num = input("what time is it? ")
    time = convert(num)
    if time >= 7 and time <= 8:
        print("Breakfast Time")
    elif time >=12 and time <=13:
        print("Lunch Time")
    elif time >= 18 and time <=19:
        print("Dinner Time")


def convert(time):
    hours, mins = time.split(":")
    mins = float(mins)/60
    return float(hours) + mins


if __name__ == "__main__":
    main()







