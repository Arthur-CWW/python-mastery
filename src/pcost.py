with open("Data/portfolio3.dat", "r") as file:
    total = 0
    for line in file:
        # print(line)
        words = line.strip().split(" ")
        # print(words)
        name, quantity, price = words
        # for quantity, price in words:
        # print(quantity, price)
        try:
            total += int(quantity) * float(price)
        except ValueError:
            print(f"Error:{name} {quantity} or {price} is not a number")
    print(total)
