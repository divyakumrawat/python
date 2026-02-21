fruit = input("enter the name of fruit: ")
color = input("enter the color of thhat fruit: ")

if fruit == "banana":
    if color == "green":
        print("unripe")
    elif color == "yellow":
        print("ripe")
    elif color == "brown":
        print("overripe")

else:
    print("no informationn for this fruit")
    
