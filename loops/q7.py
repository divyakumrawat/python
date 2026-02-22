while True:
    number = int(input("enter value between 1 and 10: "))
    if 1 <= number <= 10:
        print("thanks")
        break
    else:
        print("invalis number, try again later")